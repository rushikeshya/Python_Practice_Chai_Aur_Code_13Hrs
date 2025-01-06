

def list_all_videos(videos):
    pass

videos = []
while True:
    print("/n Youtube Manager | choose an option ")
    print("1. List a Favorite Video ")
    print("2. Add a youtub video ")
    print("3. Update a youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app ")
    choice = input("Enter your choice")

    match choice:
        case '1':
            list_all_videos(videos)
 
