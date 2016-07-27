
import media
import fresh_tomatoes

shawshank_redemption = media.Movie(
  "Shawshank Redemption",
  "Guy escapes from prison",
  "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
  "https://www.youtube.com/watch?v=TaYNFrecwpQ",
  "02/07/1999")

avatar = media.Movie(
  "Avatar",
  "Guy goes to another planet",
  "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
  "https://www.youtube.com/watch?v=5PSNL1qE6VY",
  "11/07/1989")

killbill_1 = media.Movie(
  "Kill Bill - 1",
  "Lady is pissed off and wants to bite friends",
  "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
  "https://www.youtube.com/watch?v=7kSuas6mRpk",
  "23/07/2011")

pk = media.Movie(
  "PK",
  "Human like Alien",
  "https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg",
  "https://www.youtube.com/watch?v=SOXWc32k4zA",
  "02/08/1995")

soodhu_kavvum = media.Movie(
  "Soodhu Kavvum",
  "Amateur Kidnappers",
  "https://upload.wikimedia.org/wikipedia/en/9/93/Soodhu_kavvum.jpg",
  "https://www.youtube.com/watch?v=08Ar821Av-Q",
  "12/07/2016")

special26 = media.Movie(
  "Special 26",
  "couple guys give cops a run around",
  "https://upload.wikimedia.org/wikipedia/en/7/7c/Special_26_poster.jpg",
  "https://www.youtube.com/watch?v=PiyQb28geOg",
  "04/07/1991")

movies = [shawshank_redemption, avatar, killbill_1, pk, soodhu_kavvum, special26]  # noqa

''' call to open_movies_page function in fresh_tomatoes
 file is to render and display dynamic movie trailer page. It takes the movies
 list as input.'''
fresh_tomatoes.open_movies_page(movies)
