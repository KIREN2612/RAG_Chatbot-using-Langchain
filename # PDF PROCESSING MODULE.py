# PDF PROCESSING MODULE
#-----------------------------------------------------

@time_decorator
def process_pdf(pdf_path, query, llm):
    """Process a PDF file and answer queries using LangChain"""
    logger = logging.getLogger(__name__)
    logger.info(f"Processing PDF: {pdf_path} with query: '{query}'")
    
    try:
        # 1. Load the PDF
        logger.info(f"Loading PDF file: {pdf_path}")
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        logger.info(f"PDF loaded successfully with {len(documents)} pages")

        # 2. Split the text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.split_documents(documents)
        logger.info(f"Split into {len(texts)} text chunks")

        # 3. Create embeddings
        logger.info("Creating embeddings with all-MiniLM-L6-v2")
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        # 4. Create a vector store
        logger.info("Creating FAISS vector store")
        vector_store = FAISS.from_documents(texts, embeddings)
        logger.info("Vector store created successfully")

        # 5. Create a retrieval chain
        logger.info("Setting up retrieval QA chain")
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 3})
        )

        # 6. Ask the question
        logger.info(f"Querying PDF with: '{query}'")
        result = qa_chain.invoke(query)
        logger.info("Query processed successfully")
        
        return result
        
    except Exception as e:
        error_msg = f"Error processing PDF: {str(e)}"
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        raise Exception(error_msg)

#-----------------------------------------------------