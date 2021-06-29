from process import Process
from save import Save
from extract import Extract

if __name__ == "__main__":

    url = 'http://books.toscrape.com/index.html'

    extractMainPage = Extract(url)
    extractMainPage.get_soup()
    mainPageProcess = Process(extractMainPage.soup)

    for counter, category in enumerate(mainPageProcess.soup_PagePrincipal_process()):

        category_extract = Extract(category)
        category_extract.get_soup()
        category_process = Process(category_extract.soup)

        for page in range(1, int(category_process.number_of_page()) + 1):

            if page == 1:
                page_extract = Extract(category_extract.url + 'index' + '.html')
            else:
                page_extract = Extract(category_extract.url + 'page-' + str(page) + '.html')

            page_extract.get_soup()
            category_process = Process(page_extract.soup)

            for counter, book in enumerate(category_process.soup_category_process()):
                book_extract = Extract(book)
                book_extract.get_soup()

                book_process = Process(book_extract.soup)

                Save(book_process.books_soup_process(book))
