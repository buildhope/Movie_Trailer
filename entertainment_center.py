# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

shawshank_redemption = (media.Movie("Shawshank Redemption","Guy escapes from prison",
                                    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                    "https://www.youtube.com/watch?v=TaYNFrecwpQ"))

avatar = (media.Movie("Avatar","Guy goes to another planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY"))

killbill_1 = (media.Movie("Kill Bill - 1","Lady is pissed off and wants to bite friends",
                          "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                          "https://www.youtube.com/watch?v=7kSuas6mRpk"))

pk = (media.Movie("PK","Human like Alien","https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg",
                  "https://www.youtube.com/watch?v=SOXWc32k4zA"))

soodhu_kavvum = (media.Movie("Soodhu Kavvum","Amateur Kidnappers",
                             "https://upload.wikimedia.org/wikipedia/en/9/93/Soodhu_kavvum.jpg",
                             "https://www.youtube.com/watch?v=08Ar821Av-Q"))

special26 = (media.Movie("Special 26","couple guys give cops a run around",
                         "https://upload.wikimedia.org/wikipedia/en/7/7c/Special_26_poster.jpg",
                         "https://www.youtube.com/watch?v=PiyQb28geOg"))

movies = [shawshank_redemption, avatar, killbill_1,pk,soodhu_kavvum,special26]
fresh_tomatoes.open_movies_page(movies)

