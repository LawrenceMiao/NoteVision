from bs4 import BeautifulSoup
import requests
import re
import csv

def getAllOverview(line, mappings):
    individual = line.split(':')
    text_update = individual[1].replace(" ", "")
    mappings[individual[0]] = text_update
    print(list(mappings))
    exit(1)

def containsDigit(line):
    for x in line:
        if x.isdigit():
            return True
    return False

def search(address, iteration):
    # checks to make sure address is only characters
    secondary_url = 'https://www.mass.gov{}'
    url = secondary_url.format(address)
    addressesToScrape = requests.get(url)
    # append the url to the list
    iteration.append(url)
    soup = BeautifulSoup(addressesToScrape.text, 'html.parser')

    # get phone number
    tel_links = soup.select('a[href*=tel]')
    digits = ''
    for x in tel_links[0].get_text().strip():
        if x.isdigit():
            digits += x
    iteration.append(digits)
    # get personal website link
    websiteExist = False
    links = soup.findAll('a', attrs={'class':'js-clickable-link'})
    for link in links:
        if 'Website' in link.get_text():
            websiteExist = True
            iteration.append(link.get('href'))
    if not websiteExist:
        iteration.append(None)
    # get overview information
    overview  = soup.find('section', attrs={'class':'ma__page-overview'})
    if overview:
        overview_section  = overview.find('div', attrs={'class':'ma__rich-text'})
        if overview_section:
            text_content = overview_section.get_text(separator='\n', strip=True)
            # check for No/Yes and integers
            lines = text_content.split('\n')
            mappings = {'Total Number of Units': None, 'Number of Traditional Units': None, 'Number of Special Care Units' : None, 'Low Income Options' : None}
            for line in lines:
                if containsDigit(line) or 'No' in line or 'Yes' in line or 'None' in line:
                    individual = line.split(':')
                    individual[0] = individual[0].replace("-", " ")
                    text_update = individual[1].replace(" ", "")
                    mappings[individual[0]] = text_update

            for x in mappings.values():
                iteration.append(x)
                 
    # get more-info information
    more = soup.findAll('div', attrs={'class':'ma__rich-text'})
    if more:
        for a in more:
            if 'Nonprofit' in a.get_text() or 'opened in' in a.get_text():
                lines = a.get_text().split('\n')
                x = 0
                mappings2 = {'Year': None, 'Nonprofit Ownership': None}
                for line in lines:
                    line = line.strip()
                    if line and x < 2:
                        if containsDigit(line) or 'Nonprofit Ownership' in line:
                            a = re.split(r'\s*in\s*|\s*:\s*', line)
                            for y in a:
                                y = y.replace(".", "")
                                if y.isdigit():
                                    mappings2['Year'] = y
                                elif y == 'No' or y == 'Yes' or y == 'None':
                                    mappings2['Nonprofit Ownership'] = y
                        x += 1
                for x in mappings2.values():
                    iteration.append(x)
    print(iteration)

def main():
    base_url = 'https://www.mass.gov/assisted-living/locations?page={}'
    pageNumber = 0
    storage = []
    print("Retrieving values")
    while True:
        # make new url to scape
        url = base_url.format(pageNumber)
        pageToScrape = requests.get(url)
        # check if the next page exists
        if pageToScrape.status_code == 200:
            # scrape the information
            soup = BeautifulSoup(pageToScrape.text, "html.parser")
            locations = soup.findAll('a', href=lambda href: href and '/locations' in href)

            # 
            for location in locations:
                # storage list for this iteration
                iteration = []
                # get the name of the location
                iteration.append(location.get_text().strip())
                # run a function to find specifics
                search(location['href'], iteration)
                storage.append(iteration)

            # break out if we cannot find any more pages
            if not soup.find('a', attrs={'rel':'next'}):
                print("No more pages. Exiting Loop.")
                break

            pageNumber += 1
            # helps prevent overloading pages
            # time.sleep(1)
        else:
            break

    # put it into the spread sheet
    # scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    # client = gspread.authorize(creds)
    # sheet = client.open('Homes').sheet1

    print("Updating values")
    
    # file for csv
    file_path = 'output.csv'

    # Write data to the CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(storage)


    print("Finished.")



main()