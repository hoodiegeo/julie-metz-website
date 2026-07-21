#!/usr/bin/env python3
import os

OUT = os.path.join(os.path.dirname(__file__), "site")

NAV = [
    ("index.html", "home_up.gif", "Home Page"),
    ("bio.html", "bio_up.gif", "Biography"),
    ("resume.html", "resume_up.gif", "Resume"),
    ("resume.html#recordings", "music_up.gif", "My Musical Selections"),
    ("jules.html", "jules_up.gif", "Jules Entertainment"),
    ("education.html", "education_up.gif", "Education"),
    ("violin.html", "violin_gram_up.gif", "Violin Gram"),
    ("articles.html", "articles_up.gif", "Articles"),
    ("lectures.html", "lectures_up.gif", "Lectures"),
    ("contactus2.html", "contactus_up.gif", "Contact Us"),
]

def sidebar():
    rows = "\n".join(
        f'        <tr><td><a href="{href}"><img src="btn2/{img}" alt="{alt}" width="140" height="23"></a></td></tr>'
        for href, img, alt in NAV
    )
    return f"""  <div id="sidebar1">
    <table width="152">
      <tbody>
{rows}
      </tbody>
    </table>
    <img class="violin" src="images/violin_pict.png" alt="Violin" width="126" height="73">
  </div>"""

def page(filename, title, main, extra_head="", extra_body=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Julie Metz — violin and viola performer, educator, conductor and music contractor. Owner of Jules Entertainment, providing musical services for special occasions.">
<link rel="stylesheet" href="style.css">
{extra_head}</head>
<body>
<div id="container">
  <div id="header"></div>
{sidebar()}
  <div id="mainContent">
{main}
  </div>
  <br class="clearfloat">
  <div id="footer">
    <p class="style1">Copyright &copy;2024 Jules Entertainment<br><br>
      Julie Metz &nbsp;&bull;&nbsp; 310.467.0564 &nbsp;&bull;&nbsp;
      <a href="mailto:2julie@fea.net">2julie@fea.net</a></p>
  </div>
</div>
{extra_body}</body>
</html>
"""
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)
    print("wrote", filename)

# ---------- HOME ----------
slides = ["metz4.jpg","metz1.jpg","metz5.jpg","metz0.jpg","metz6.jpg","regis.jpg","metz3.jpg"]
imagearray = ",\n".join(f'\t\t["images/{s}", "", "_self", ""]' for s in slides)
home_head = """<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script src="fadeslideshow.js"></script>
<style>#fadeshow1{margin:0 auto;}</style>
"""
home_body = f"""<script>
var mygallery=new fadeSlideShow({{
	wrapperid: "fadeshow1",
	dimensions: [400, 400],
	imagearray: [
{imagearray}
	],
	displaymode: {{type:'auto', pause:3400, cycles:0, wraparound:false}},
	persist: false,
	fadeduration: 1200,
	descreveal: "ondemand",
	togglerid: ""
}})
</script>
"""
home_main = """    <div style="display:flex; flex-wrap:wrap; gap:24px; align-items:flex-start; justify-content:center;">
      <div id="fadeshow1" style="position:relative; width:400px; height:400px; background:#000; overflow:hidden;"></div>
      <div style="display:flex; flex-direction:column; gap:16px; align-items:center;">
        <a href="https://www.youtube.com/watch?v=JKV1Pj4O0tY" target="_blank" rel="noopener"><img src="images/strings_r_us.png" alt="Strings R' Us" width="165" height="119" style="border:0;"></a>
        <a href="jules.html"><img src="images/side_pict1.png" alt="Music Masters" width="165" height="119" style="border:0;"></a>
        <a href="lectures.html"><img src="images/side_pict2.png" alt="Lectures" width="165" height="119" style="border:0;"></a>
      </div>
    </div>
"""
page("index.html", "Jules Entertainment, Julie Metz, Julie Metz Violin, Viola, Educator, Conductor and Contractor",
     home_main, home_head, home_body)

# ---------- BIOGRAPHY ----------
bio = """    <h1>Biography</h1>
    <img class="biopic" src="images/juliebio.jpg" alt="Julie Metz" width="220">
    <p>Julie Metz&rsquo;s passion for music is evident in its great versatility as well as substance. As a violin and viola performer, Julie has worked with major symphonies and recording artists from around the world. As an educator, she has led pre-concert lectures, created instrumental and music appreciation curriculum, coordinated music programs and taught over 5000 elementary and secondary students and adults.</p>
    <p>Julie has worked with the Los Angeles Music Center Opera, Opera Pacific, Santa Fe Opera, North Carolina Opera, Long Beach Symphony, Pacific Symphony Orchestra, San Diego Symphony, Lake Charles, Louisiana Symphony, Laredo, Texas Symphony and The Fresno Philharmonic. She has toured the world extensively with Yanni and his Orchestra, performing in over 200 concerts and three videos.</p>
    <p>As a free-lance musician, Julie has accompanied such popular performers as: Glen Campbell, Crystal Gayle, Neil Sedaka, Bernadette Peters, The Temptations, Andy Williams, The 5th Dimension, Art Garfunkel, and Paul Anka. Julie continues to perform as a recitalist and lecturer as well as provide music for the latest Broadway shows.</p>
    <p>While still a student, Julie was the violin soloist and consultant for the CBS-Television Movie of the Week, &ldquo;Running Out.&rdquo; As a member of the Motion Picture, Television and Recording Industries, she has played on numerous television shows, cartoons, videos, films and commercials.</p>
    <p>Julie was the recipient of the Outstanding Teacher Award from the Anaheim Union High School District in 2010 and the Outstanding Contributions to Education Award from the Orange County Department of Education in 2009. She was nominated in 2008 for the Orange County Arts Award for Outstanding Individual Artist. Julie received the Honorary Service Award from the El Dorado O&rsquo;este PTA Council in 2007 and the Outstanding Music Educator Award from the Pacific Symphony Orchestra in 2000.</p>
    <p>She has taught students both privately and within the public and private school systems, in orchestral institutes, chamber ensembles, music camps and training programs. In addition, she has initiated innovative educational programs as well as expanded upon existing ones. Julie has implemented grants and managed programs whereby she was responsible for overseeing up to thirty musicians.</p>
    <p>Julie creates and develops educational programs for orchestras. For the last 18 years, she has coordinated and taught instrumental strings and music appreciation to 4th through 6th grade students in the Savanna School District in Anaheim, California in the respected Music Masters Program. In addition, she also coordinates the Gifted and Talented Orchestra of the Anaheim Union High School District. She has contributed her talents by writing music appreciation curriculum for the Los Angeles Philharmonic and Long Beach Symphony for use in the elementary, middle, and secondary schools.</p>
    <p>Julie has been a pre-concert lecturer with the Pacific Symphony Orchestra in Orange County, California and the Rochester Symphony. She was also the host of the popular &ldquo;Meet the Musicians&rdquo; series at the Orange County Performing Arts Center. Julie is the owner of Jules Entertainment, which provides musical services for special occasions.</p>
    <p>A graduate of the Mannes College of Music (B.M.) and the Manhattan School of Music (M.M.), Julie&rsquo;s teachers have included Glenn Dicterow (Concertmaster, New York Philharmonic), Sally Thomas, Irving Geller (Associate Concertmaster, Los Angeles Philharmonic, Retired) and Joyce Robbins (Metropolitan Opera, Retired). Her conducting teacher was Don Ray, Music Supervisor for the CBS Television Studios.</p>
    <p>Julie lives in Los Angeles, California where she enjoys gardening, bicycling and doing projects around the house.</p>
"""
page("bio.html", "Julie Metz | Biography", bio)

# ---------- RESUME ----------
music = [
    ("Beethoven, Symphony #9 - Violin excerpt","music/beethoven9.mp3"),
    ("Mendelssohn, Midsummer's Night Dream Scherzo - Violin excerpt","music/mendelssohn.midsummer.mp3"),
    ("Berlioz, Roman Carnival overture - Viola excerpt","music/berlioz.carnival.mp3"),
    ("Shostakovich, Symphony #5 - Viola excerpt","music/shostakovich5.mp3"),
    ("Violin Concerto #2 by Florence Price","music/price.violin2.mp3"),
    ("Elfentanz by Florence Price","music/price.elfentanz.mp3"),
    ("La Paix by Leo Delibe","music/lapaix.mp3"),
    ("Sarabande from the C Major Suite #3 by Bach","music/sarabande.mp3"),
    ("Exposition from the Viola Concerto by Bartok","music/bartok.mp3"),
    ("Exposition from the Viola Concerto by Stamitz","music/stamitz.mp3"),
    ("Violin Concerto (1st Movement) by Jean Sibelius","music/sibelius.mp3"),
    ("Syncopation by Fritz Kreisler","music/syncopation.mp3"),
    ("Caprice #14 by Niccol&ograve; Paganini","music/caprice14.mp3"),
    ("The Girl with the Flaxen Hair by Claude Debussy","music/thegirlwiththeflaxenhair.mp3"),
    ("Kol Nidre by Max Bruch","music/kolnidre.mp3"),
    ("Aubade by Gabriel Faure","music/aubade.mp3"),
    ("Beau Soir by Debussy - Heifetz","music/beausoir.mp3"),
    ("Le Petit Ane Blanc by Jacques Ibert","music/lepetitane.mp3"),
    ("Garden Scene by Erich Wolfgang Korngold","music/gardenscene.mp3"),
    ("Meditation by Massenet","music/meditation.mp3"),
    ("Gestillte Sehnsucht (Longing at Rest) by Johannes Brahms","music/zwei_gesange.mp3"),
]
music_items = "\n".join(f'      <li><a href="{h}">{t}</a></li>' for t,h in music)
resume = f"""    <div align="center"><img src="images/resume_title.png" alt="Julie Metz Resume" style="max-width:100%;"></div>
    <h2>Violin / Viola</h2>
    <p><a href="resume1.html">Educator, and Coordinator of Orchestral Programs</a><br>
       <a href="resume3.html">Performance Artist: Stage, Television, Video, Radio, &amp; Recording</a></p>
    <h2 id="recordings">Listen to my music selections</h2>
    <ul class="linklist">
{music_items}
    </ul>
"""
page("resume.html", "Julie Metz | Resume", resume)

# ---------- JULES ENTERTAINMENT ----------
jules = """    <div align="center">
      <img class="article-img" src="images/jules_entertainment_article.png" alt="Jules Entertainment — professional union musicians for weddings, concerts in the home, ViolinGram and the Cohen-Metz Duo. Licensed by the state of California. Call 310-467-0564.">
      <p style="margin-top:20px;"><strong>Click a link for more information:</strong><br>
        Weddings &nbsp;|&nbsp; Concerts in the Home &nbsp;|&nbsp;
        <a href="violin.html">ViolinGram</a> &nbsp;|&nbsp; Cohen-Metz Duo</p>
    </div>
"""
page("jules.html", "Jules Entertainment", jules)

# ---------- EDUCATION ----------
edu_links = [
    ("Photo Gallery","photos.html"),
    ("Music Masters","masters_article.html"),
    ("Music Masters - Buena Park Independent and Orange County News (2006)","masters_article.html"),
    ("GATE Orchestra","gate_orchestra.html"),
    ("Gate Orchestra - Orange County Register Article (2006)","gate_orchestra2.html"),
    ("Strings R' Us","https://www.youtube.com/watch?v=JKV1Pj4O0tY"),
    ("Strings R' Us Brochure","brochures.html"),
    ("Adult Education","adult.html"),
    ("Curriculum Writer","curriculum_writer.html"),
    ("Youth Orchestra Conductor","youth_orchestra.html"),
    ("Youth Orchestra Program Activities","orchestra_programs.html"),
    ("Bach to Basic: The Story and Music of Johann Sebastian Bach - Anaheim Independent Article (5/13)","auhsdorchestra.anaheimindependent.pdf"),
]
edu_items = "\n".join(f'      <li><a href="{h}">{t}</a></li>' for t,h in edu_links)
edu = f"""    <h1>Education</h1>
    <div align="center"><img class="article-img" src="images/classroom_sample3.png" alt="Ms. Metz's classroom" style="max-width:100%;"></div>
    <p style="text-align:center;">A look through Ms. Metz&rsquo;s classroom &mdash; explore the programs below.</p>
    <ul class="linklist">
{edu_items}
    </ul>
"""
page("education.html", "Julie Metz | Education", edu)

# ---------- VIOLIN GRAM ----------
violin = """    <div align="center">
      <img class="article-img" src="images/violin_gram3.png" alt="Say it with a ViolinGram. For $150.00 your Sweetie will receive a scroll with your special message, a rose and a violinist playing up to 3 songs. Perfect for Valentine's Day, Birthday, Anniversary, Engagement and Invitations. Call 310-467-0564.">
    </div>
"""
page("violin.html", "Violin Gram", violin)

# ---------- ARTICLES ----------
articles = """    <div align="center"><img src="images/articles_titrle.png" alt="Articles" style="max-width:100%;"></div>
    <ul class="linklist">
      <li><a href="article_one.html">Article #1 - A Letter From The Musician's Lips</a></li>
      <li><a href="article_two.html">Article #2 - Miller Children's Hospital</a></li>
    </ul>
"""
page("articles.html", "Julie Metz | Articles", articles)

# ---------- LECTURES ----------
lectures = """    <div align="center"><img src="images/lectures_title.png" alt="Lectures" style="max-width:100%;"></div>
    <ul class="linklist">
      <li><a href="orchestral.html">Orchestral</a></li>
      <li><a href="life_love_remembrance.html">Life, Love and Remembrance</a></li>
      <li><a href="cohen_metz_duo.html">Cohen/Metz Duo</a></li>
      <li><a href="preconcert_one.html">Pre-Concert Lecturer</a></li>
      <li><a href="preconcert_two.html">Music For Pre-Concert Lectures</a></li>
    </ul>
"""
page("lectures.html", "Julie Metz | Lectures", lectures)

# ---------- CONTACT ----------
contact = """    <h1>How to Contact Us</h1>
    <div style="display:flex; flex-wrap:wrap; gap:24px; align-items:center;">
      <img src="images/jules_pict10.png" alt="Jules Entertainment" style="max-width:220px;">
      <div>
        <p style="font-size:1.2em; line-height:1.8;">
          <strong>Julie Metz</strong><br>
          310.467.0564<br>
          <a href="mailto:2julie@fea.net">2julie@fea.net</a>
        </p>
        <p><strong>Check us out!</strong><br>
          <a href="http://www.facebook.com/profile.php?id=1642994176" target="_blank" rel="noopener"><img src="images/facebook_logo.png" alt="Facebook" style="border:0;"></a>
        </p>
      </div>
    </div>
"""
page("contactus2.html", "Julie Metz | Contact Us", contact)

print("done")
