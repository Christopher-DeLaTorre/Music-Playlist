from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    if self.__first_song == None:
      self.__first_song = Song(title)
    else:
      song = self.__first_song
      while song._Song__next_song != None:
        song = song.get_next_song()
      song.set_next_song(title)


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

  def find_song(self, title):
    song = self.__first_song
    index = 0
    while song.get_next_song() != None:
      if song.get_title() == title:
        return index
      else:
        index += 1
        song = song._Song__next_song
    return -1
   


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    song = self.__first_song
    if song.get_title() == title:
      print("removed!")   
      self.__first_song = song.get_next_song()
      return

    while song != None:
      if song.get_next_song() == title:
        print("removed!")
        song.set_next_song(song.get_next_song().get_next_song()) 
        return
      song = song._Song__next_song

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    song = self.__first_song
    index = 1
    while song.get_next_song() != None:
      index += 1
      song = song.get_next_song()
    return index


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    if self.__first_song == None:
      print('No songs')
      return
    index = 1 
    song = self.__first_song
    while song != None:
      print(f'{index}. {song.get_title()}')
      song = song._Song__next_song
      index += 1