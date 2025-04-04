# MEMORY MANAGER MODULE
#-----------------------------------------------------

def create_memory():
    """Create a new conversation memory object"""
    logger = logging.getLogger(__name__)
    logger.info("Creating new conversation memory")
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="output"
    )
    return memory

def add_to_memory(memory, user_input, response):
    """Add a conversation turn to memory"""
    logger = logging.getLogger(__name__)
    logger.info("Adding conversation turn to memory")
    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(response)
    
def get_conversation_history(memory):
    """Get formatted conversation history from memory"""
    logger = logging.getLogger(__name__)
    logger.info("Retrieving conversation history")
    return memory.buffer

#-----------------------------------------------------