#! python3
import sys
import webbrowser

POSTAL_ABBREVIATIONS = {
    "ontario": "on",
    "quebec": "qc",
    "nova scotia": "ns",
    "new brunswick": "nb",
    "manitoba": "mb",
    "british columbia": "bc",
    "prince edward island": "pe",
    "saskatchewan": "sk",
    "alberta": "ab",
    "newfoundland and labrador": "nl"
}

args = sys.argv  # ['job_search_canada.py','bc,vancouver','python','developer']
if len(args) < 3:
    raise SystemExit("usage: $:python job_search_canada.py province_code,city  job_title")
place_input = args[1].split(',')
job_title_input = args[2:]


def get_indeed_url(place, job):
    """
    Opens a indeed tab in the default browser with job search results
    :param place: string, the place. Ie, "bc,vancouver"
    :param job: string, the job title. Ie, "software developer"
    """
    province = place[0].replace(' ', '+')
    if len(province) > 2:
        province = POSTAL_ABBREVIATIONS[province.lower()].upper()
    city = place[1].replace('.', '+') if len(place) > 1 else None
    job_title = "+".join(job)
    location = province.title()
    if city:
        location = "{}%2C+{}".format(city.title(), province.upper())
    indeed_url = 'https://ca.indeed.com/jobs?q={}&l={}'.format(job_title, location)

    webbrowser.open(indeed_url)
    return indeed_url


def get_linkedin_url(place, job):
    """
    Opens a LinkedIn tab in the default browser with job search results
    :param place: string, the place. Ie, "bc,vancouver"
    :param job: string, the job title. Ie, "software developer"
    """
    province = (place[0].replace('.', '%20')).title()
    city = (place[1].replace('.', '%20')).title() if len(place) > 1 else False
    location = "{}%2C%20{}%2C%20Canada".format(city, province) if city else province
    job_title = "%20".join(job)
    linkedin_url = 'https://www.linkedin.com/jobs/search/?keywords={}&location={}'.format(job_title, location)
    webbrowser.open(linkedin_url)
    return linkedin_url


get_linkedin_url(place_input, job_title_input)
get_indeed_url(place_input, job_title_input)
