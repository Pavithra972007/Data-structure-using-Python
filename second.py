# Music Playlist using Singly Linked List

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # Create Playlist
    def create_playlist(self):
        n = int(input("Enter the number of songs: "))
        for i in range(n):
            song = input(f"Enter song {i + 1}: ")
            self.insert_song(song)

    # Insert Song
    def insert_song(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Song added successfully!")

    # Delete Song
    def delete_song(self, song):
        temp = self.head

        if temp is None:
            print("Playlist is empty.")
            return

        if temp.song == song:
            self.head = temp.next
            print("Song deleted successfully!")
            return

        prev = None
        while temp and temp.song != song:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Song not found.")
            return

        prev.next = temp.next
        print("Song deleted successfully!")

    # Display Playlist
    def display_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        print("\nMusic Playlist:")
        temp = self.head
        while temp:
            print(temp.song)
            temp = temp.next


# Main Program
playlist = Playlist()

while True:
    print("\n--- Music Playlist Menu ---")
    print("1. Create Playlist")
    print("2. Insert Song")
    print("3. Delete Song")
    print("4. Display Playlist")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        playlist.create_playlist()

    elif choice == 2:
        song = input("Enter song name to insert: ")
        playlist.insert_song(song)

    elif choice == 3:
        song = input("Enter song name to delete: ")
        playlist.delete_song(song)

    elif choice == 4:
        playlist.display_playlist()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
