import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
chatMsg = raw_input(“Enter a message: “)
whilechatMsg != “/exit”:
    mc.postToChat(chatMsg)
    chatMsg = raw_input(“Enter a message: “)
