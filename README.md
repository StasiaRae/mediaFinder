# mediaFinder

A Python script that searches through directories and subdirectories looking for files with certain extensions.
By default, it is configured to search for .mp3, .mp4, and .jpg files. Only supports Windows.

#Usage

Script should be run from the command line.
A parameter can be passed to specify which path to look in.
If no paramter is passed, it will look in the current directory.

Example usage:
```
C:\User> python mediaFinder.py C:\Music

C:\Music\song.mp3
C:\Music\art.jpg
C:\Music\video.mp4
C:\Music\Favorites\1985\song2.mp3
```

#mediaDirectoryFinder

Similar to mediaFinder, but only prints names of directories that have files of the desired extensions.

Example usage:
```
C:\User> python mediaFinder.py C:\Music

C:\Music\
C:\Music\Favorites\1985\
```
