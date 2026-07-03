class Message:
    msgcounter=0
    def __init__(self,sender,content):
        self.sender=sender
        self.content=content
        self.id=Message.msgcounter
        Message.msgcounter+=1

    def __str__(self):
        return f"({self.id}) {self.sender}:{self.content}"
    
class User:
    def __init__(self,username):
        self.username=username
        self.chatroom=None
        self.user_msgs=[]

    def join_chatroom(self,chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom")
        else:
            self.chatroom=chatroom
            chatroom.add_user(self.username)
            print(f"{self.username} has been added to {chatroom}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom")
        else:
            self.chatroom.remove_user(self.username)
            print(f"{self.username} was removed from {self.chatroom}")
            self.chatroom=None

    def send_msg(self,content):
        if self.chatroom:
            self.chatroom.broadcast(self.username,content)
            self.user_msgs.append(content)
        else:
            print(f"{self.username} is not in any chatroom")
    
    def user_history(self):
        print(f"Message history for {self.username}:")
        for msg in self.user_msgs:
            print(msg)

class ChatRoom:
    def __init__(self,room):
        self.room=room
        self.users=[]
        self.msgs=[]

    def add_user(self,user):
        self.users.append(user)

    def remove_user(self,user):
        self.users.remove(user)

    def broadcast(self,sender,content):
        msg = Message(sender,content)
        print(msg)
        self.msgs.append(msg)

    def msg_history(self):
        print(f"Message history for chatroom {self.room}:")
        for msg in self.msgs:
            print(msg)

u1=User("Alice")
u2=User("Bob")
cr=ChatRoom("General")
u1.join_chatroom(cr)
u2.join_chatroom(cr)
u1.send_msg("Hello everyone!")
u2.send_msg("Hi Alice!")
u1.user_history()
cr.msg_history()
cr.broadcast("System","This is a system message.")
