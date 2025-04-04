# CHATBOT MODULE
#-----------------------------------------------------

@time_decorator
def chatbot(llm, query, memory=None, pdf_context=False, pdf_file=None):
    """Process a query using the LLM, optionally with PDF context and memory"""
    logger = logging.getLogger(__name__)
    logger.info(f"Processing query: '{query}' (PDF context: {pdf_context})")
    
    try:
        if pdf_context and pdf_file:
            # Use Langchain with PDF context
            result = process_pdf(pdf_file, query, llm)
            response = result['result']
        else:
            # Use direct LLM query with memory if available
            if memory:
                # Format prompt with conversation history
                memory.chat_memory.add_user_message(query)
                formatted_prompt = memory.buffer
                response = llm.invoke(formatted_prompt)
                memory.chat_memory.add_ai_message(response)
            else:
                response = llm.invoke(query)
                
        logger.info(f"Generated response (length: {len(response)})")
        return response
    except Exception as e:
        error_msg = f"Error processing query: {str(e)}"
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        return f"I encountered an error: {str(e)}. Please try again or rephrase your question."

@time_decorator
def test_basic_llm(llm):
    """Test the basic LLM with a simple query"""
    logger = logging.getLogger(__name__)
    test_query = "What's the capital of France?"
    logger.info(f"Testing basic LLM with query: {test_query}")
    
    try:
        print("Basic LLM Response:")
        response = llm.invoke(test_query)
        print(response)
        logger.info("Basic LLM test completed successfully")
        return response
    except Exception as e:
        logger.error(f"Error testing basic LLM: {str(e)}")
        print(f"Error testing LLM: {str(e)}")
        return None

@time_decorator
def interactive_chatbot(llm):
    """Run an interactive chatbot session with memory"""
    logger = logging.getLogger(__name__)
    print("\n=== Interactive Chatbot ===")
    print("Type 'exit' to quit")
    print("Type 'pdf' to switch to PDF context mode")
    print("Type 'memory on/off' to toggle conversation memory")
    print("Type 'clear' to clear conversation history")
    
    mode = "direct"
    pdf_file = None
    memory_enabled = True
    memory = create_memory()
    
    logger.info("Starting interactive chatbot session")
    
    while True:
        prefix = "You (PDF mode): " if mode == "pdf" else "You: "
        user_input = input(f"\n{prefix}")
        
        # Handle special commands
        if user_input.lower() == 'exit':
            logger.info("Exiting interactive chatbot")
            break
            
        elif user_input.lower() == 'pdf':
            if mode == "direct":
                print("Switching to PDF context mode. Please upload a PDF.")
                try:
                    uploaded = files.upload()
                    if uploaded:
                        pdf_file = list(uploaded.keys())[0]
                        mode = "pdf"
                        logger.info(f"Switched to PDF mode with file: {pdf_file}")
                    else:
                        print("No file uploaded. Staying in direct mode.")
                except Exception as e:
                    logger.error(f"Error uploading PDF: {str(e)}")
                    print(f"Error uploading PDF: {str(e)}")
            else:
                mode = "direct"
                logger.info("Switched to direct mode")
                print("Switching to direct mode.")
            continue
            
        elif user_input.lower() == 'memory on':
            memory_enabled = True
            print("Conversation memory enabled.")
            logger.info("Conversation memory enabled")
            continue
            
        elif user_input.lower() == 'memory off':
            memory_enabled = False
            print("Conversation memory disabled.")
            logger.info("Conversation memory disabled")
            continue
            
        elif user_input.lower() == 'clear':
            memory = create_memory()  # Create a new memory object
            print("Conversation history cleared.")
            logger.info("Conversation history cleared")
            continue
        
        # Process user query
        start_time = time.time()
        
        response = chatbot(
            llm, 
            user_input, 
            memory=memory if memory_enabled else None,
            pdf_context=(mode == "pdf"), 
            pdf_file=pdf_file
        )
        
        processing_time = time.time() - start_time
        
        print(f"Bot: {response}")
        print(f"[Response time: {processing_time:.2f} seconds]")
        
        # Log performance metrics
        logger.info(f"Query processed in {processing_time:.2f} seconds")

#-----------------------------------------------------