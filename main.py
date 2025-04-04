# MAIN MODULE
#-----------------------------------------------------

def main():
    """Main application entry point"""
    # Set up logging
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting LangChain PDF Chatbot application")
    
    try:
        # Initialize LLM
        llm = initialize_llm()
        logger.info("LLM initialized successfully")
        
        # Test the basic LLM
        test_basic_llm(llm)
        
        # Optionally start the interactive chatbot
        interactive_chatbot(llm)
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        print(f"Application error: {str(e)}")

if __name__ == "__main__":
    main()
