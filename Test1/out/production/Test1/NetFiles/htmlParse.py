from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        print ("Encountered comment:", data)
        pos = self.getpos()
        print ("At line: ", pos[0], " position ", pos[1])

def main():
    parser = MyHTMLParser()




    # open the sample HTML file and read it
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)


main()