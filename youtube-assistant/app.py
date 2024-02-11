import main as youtube
import textwrap

# Add your YouTube video URL
youtube_url="https://www.youtube.com/watch?v=1p6P471PBx0"

# Different Queries
query="What did Satya say about AI?"
#query = "How old is Satya in 2024?"
#query="Did Satya mention Google?"
#query="Did Satya mention anything about TikTok?"

if query and youtube_url:
  db = youtube.create_db_from_youtube_video_url(youtube_url)
  response, docs = youtube.get_response_from_query(db, query)
  print(textwrap.fill(response, width=100))