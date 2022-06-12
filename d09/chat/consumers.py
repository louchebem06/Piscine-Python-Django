import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message, ChatRoom

class ChatConsumer(WebsocketConsumer):

	def connect(self):
		self.room_group_name = 'master'
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
		)
		user = self.scope['user']
		username = user.username
		message = "has joined the chat"
		room = self.scope['path'].lstrip("/")
		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type' : 'chat_message',
				'message' : message,
				'room' : room,
				'user':user.username
			}
		)
		msg = Message()
		msg.user = user
		msg.room = ChatRoom.objects.get(name=room)
		msg.msg = message
		msg.save()
		self.accept()

	def disconnect(self, close_code):
		user = self.scope['user']
		username = user.username
		message = "has left the chat"
		room = self.scope['path'].lstrip("/")
		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type' : 'chat_message',
				'message' : message,
				'room' : room,
				'user': user.username
			}
		)
		msg = Message()
		msg.user = user
		msg.room = ChatRoom.objects.get(name=room)
		msg.msg = message
		msg.save()

	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		room = text_data_json['room']
		user = self.scope['user']
		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type' : 'chat_message',
				'message' : message,
				'room' : room,
				'user' : user.username
			}
		)
		msg = Message()
		msg.user = self.scope['user']
		msg.room = ChatRoom.objects.get(name=room)
		msg.msg = message
		msg.save()
	
	def chat_message(self, event):
		message = event['message']
		room = event['room']
		user = event['user']

		self.send(text_data=json.dumps({
			'type' : 'chat',
			'message' : message,
			'room' : room,
			'user' : user
		}))
