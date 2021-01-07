import webbrowser, sys

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

args = sys.argv # ['web_browser_module.py','montreal','QC','python','developer']
place_input = args[1].split(',')
job_title_input = args[2:]



def get_indeed_url(place, job):
    """
    Returns a website url to search jobs
    :param province:
    :param job_title:
    :param city:
    :return:
    """
    province = place[0].replace('.', '+')
    city = place[1].replace('.', '+') if len(place) > 1 else False
    job_title = "+".join(job)
    location = "{}%2C+{}".format(city.title(), POSTAL_ABBREVIATIONS[province.lower()].upper()) if city else province.title()
    indeed_url = 'https://ca.indeed.com/jobs?q={}&l={}'.format(job_title, location)

    webbrowser.open(indeed_url)
    return indeed_url


def get_linkedin_url(place, job):
    province = (place[0].replace('.', '%20')).title()
    city = (place[1].replace('.', '%20')).title() if len(place) > 1 else False
    location = "{}%2C%20{}%2C%20Canada".format(city, province) if city else province
    job_title = "%20".join(job)
    linkedin_url = 'https://www.linkedin.com/jobs/search/?keywords={}&location={}'.format(job_title, location)
    webbrowser.open(linkedin_url)
    return linkedin_url


get_indeed_url(place_input, job_title_input)
get_linkedin_url(place_input, job_title_input)
