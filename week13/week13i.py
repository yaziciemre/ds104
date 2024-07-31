
# The codes below must be in two different files

from kafka import KafkaProducer # INSERT, CREATE, PRODUCE

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send messages to the topic
for i in range(10):
    producer.send('my_topic', key=bytes(str(i), 'utf-8'), value=bytes(f'message {i}', 'utf-8'))
    producer.flush()

producer.close()


# ======================
from kafka import KafkaConsumer # reader

# Create a Kafka consumer
consumer = KafkaConsumer(
    'my_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='python-consumer'
)

# Read messages from the topic
for message in consumer:
    print(f'Received message: {message.value.decode("utf-8")} from topic: {message.topic}')

consumer.close()




"""

INSERT INTO table (name, ...., hobbies) VALUES ('Emre', 34, [electronic, chess])

"""

INSERT INTO posts (title, ...) VALUES ('xxx', '')

db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date(),
  support: 33
})


NON FIXED
NON CONSTANT


SELECT * FROM posts WHERE category = 'News'
db.posts.find( {category: "News"} )


