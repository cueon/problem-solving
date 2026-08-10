'''
playByGenre = {
    "classic": 1450,
    "pop": 3100
}

songsByGenre = {
    "classic": [(500, 0), (150, 2), (800, 3)],
    "pop": [(600, 1), (2500, 4)]
}
'''

def solution(genres: list[str], plays: list[int]):
    
    playByGenre = {}
    for genre, play in zip(genres, plays):
        playByGenre[genre] = playByGenre.get(genre, 0) + play
    
    songsByGenre = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in songsByGenre:
            songsByGenre[genre] = []
        songsByGenre[genre].append((play, i))
    
    playByGenre = sorted(
        playByGenre.items(), key=lambda x: x[1], reverse=True
    )
    
    playlist = []
    
    for genre, total in playByGenre:
        songs = songsByGenre[genre]
        songs.sort(key=lambda x: (-x[0], x[1]))
        for play, i in songs[:2]:
            playlist.append(i)
    
    return playlist
