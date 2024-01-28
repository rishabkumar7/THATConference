import main as youtube
import textwrap


youtube_url="https://www.youtube.com/watch?v=1p6P471PBx0"
query="What did Satya say about AI?"

if query and youtube_url:
  db = youtube.create_db_from_youtube_video_url(youtube_url)
  response, docs = youtube.get_response_from_query(db, query)
  print(textwrap.fill(response, width=100))