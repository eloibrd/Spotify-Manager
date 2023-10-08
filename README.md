# Spotify Playlist Manager

### Table of content

- [Introduction](#intro)
- [Current setup](#current)
- [Workflows](#workflows)

<a name="intro" />

## Introduction

The aim of this project is to manage my spotify playlist through scheduled workflows.

<a name="current" />

## Current setup

### Yearly playlist

Every new year, a playlist for the following year will be created.

### Current playlist

I add songs to a single playlist, every week it is cleared and every song in it is moved to the yearly playlist, duplicates are skipped.

To easily keep songs that i still wanna listen without having to add them back at the start of the week, every song that I like (unsing liked tracks) is not cleared from the current playlist.

Liked tracks are not synced in the current playlist though.

<a name="workflows" />

## Workflows

There are currently 3 workflows.

### Yearly playlist setup

Running : every new year.

```mermaid
flowchart LR
  subgraph dag[DAG]
    direction LR
    login[login to spotify]
    create[create new year playlist]
    success[do nothing on success]
    fail[send alert on failure]

    login --> create
    create --> success
    create --> fail
  end
```

### Yearly playlist update

Running : every week.

```mermaid
flowchart LR
  subgraph dag[DAG]
    direction LR
    login[login to spotify]

    subgraph foreach[for every song in the current playlist]
      direction LR
      add_song[add song to the yearly playlist]
      skip[skip song if duplicate]

      add_song --> skip
    end

    success[do nothing on success]
    fail[send alert on failure]

  login --> foreach
  foreach --> success
  foreach --> fail
  end
```

### Current playlist update

Running : every week AFTER yearly playlist update.

```mermaid
flowchart LR
  subgraph dag[DAG]
    direction LR
    login[login to spotify]

    fetch_current[fetch current playlist content]
    fetch_liked[fetch liked songs]
    trim_current[remove liked tracks from the list]

    subgraph foreach[for each track still in the list]
      remove[remove track from the current playlist]
    end

    success[do nothing on success]
    fail[send alert on failure]

  login --> fetch_current
  fetch_current --> fetch_liked
  fetch_liked --> trim_current
  trim_current --> foreach
  foreach --> success
  foreach --> fail
  end
```
