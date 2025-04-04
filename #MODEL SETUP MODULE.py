 #MODEL SETUP MODULE
#-----------------------------------------------------

@time_decorator
def initialize_llm(model_id="tiiuae/falcon-7b-instruct"):
    """Initialize and return a LangChain HuggingFacePipeline LLM"""
    logger = logging.getLogger(__name__)
    logger.info(f"Initializing LLM with model: {model_id}")
    
    try:
        # Load tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        logger.info("Tokenizer loaded successfully")
        
        # Load model with 8-bit quantization
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            load_in_8bit=True,  # Use 8-bit quantization to save memory
        )
        logger.info("Model loaded successfully with 8-bit quantization")
        
        # Create text generation pipeline
        text_generation_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=512,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.15
        )
        logger.info("Text generation pipeline created")
        
        # Initialize LangChain with the Hugging Face pipeline
        llm = HuggingFacePipeline(pipeline=text_generation_pipeline)
        logger.info("LangChain HuggingFacePipeline initialized")
        
        return llm
        
    except Exception as e:
        logger.error(f"Error initializing LLM: {str(e)}")
        raise Exception(f"Failed to initialize LLM: {str(e)}")

#-----------------------------------------------------