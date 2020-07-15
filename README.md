# Stealing Audiobooks
I should probably explain this eh?

So I was scrolling around [Scribd](https://www.scribd.com/) and listening to audiobooks (I have a membership) and found out that there was get requests and there urls was for mp3s for each chapter.

So I made a quick mitmdump + python script that catches all the scribd mp3s and prints them as a list.

**You shouldn't use this. It's probably illegal.**
# How To Use
**For this to work it does require that you have a membership and an account for scribd.**
1. Install [mitmproxy](https://mitmproxy.org/), for your operating system. Make sure you can catch the get requests.
2. Run the script using `mitmdump -q -s audiobook.py`.
3. Login to scribd.
4. Find and audiobook.
5. Wait for the audiobook chapter to load.
6. Click on the next chapter button.
7. Repeat 5. to 6. until the audiobook is finished.
8. Download all the mp3s in links.
9. Use ffmpeg to combine them.
