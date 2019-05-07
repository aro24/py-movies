from media import Media
movies= []

class Movie(Media):
    def __init__(self, title, yr, dirtr, run):
        super().__init__(title)

        self.Year = yr
        self.Director = dirtr
        self.Runtime = run

    def __repr__(self):
        return "<Movie: "+self.title+">"

    def __str__(self):
        return "("+str(self.Year)+") "+self.title

    def abbreviation(self):
        abbrev = self.slug()
        abbrev = abbrev.replace('-', '')
        return abbrev[0:3]

def section_head(msg):
    def decorator(og_funct):
        def wrap(*args, **kwargs):
            print("=====\n%s\n=====" % msg)
            return og_funct(*args, **kwargs)
        return wrap
    return decorator

@section_head("Before Year:")
def before_year(yr):
    result = [mov for mov in movies if mov.Year < yr]
    for res in result:
        print(res)

@section_head("Abbreviations:")
def abbr():
    result = [tit.abbreviation() for tit in movies]
    for res in result:
        print(res)

@section_head("Slugs:")
def slugs():
    result = [tit.slug() for tit in movies]
    for res in result:
        print(res)

def main():
    print("Thanks for checking the Local Movie Database!")
    slugs()
    abbr()
    before_year(2009)
    print("\nThank you")


if __name__ == '__main__':
    movie1 = Movie("The Room", 2003, "Tommy Wiseau", 1.65)
    movies.append(movie1)
    movie2 = Movie("Foodfight!", 2012, "Lawrence Kasanof", 1.45)
    movies.append(movie2)
    movie3 = Movie("Bee Movie", 2007, "Simon J. Smith", 1.45)
    movies.append(movie3)
    movie4 = Movie("Birdemic: Shock and Terror", 2010, "James Nguyen", 1.55)
    movies.append(movie4)
    movie5 = Movie("The Smash Brothers", 2013, "Travis Beauchamp", 4.03)
    movies.append(movie5)

    main()
