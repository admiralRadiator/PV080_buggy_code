import sys
import yaml
import flask

app = flask.Flask(__name__)


def safe_input(prompt):
    if sys.version_info[0] < 3:  # Python 2
        return raw_input(prompt)
    else:  # Python 3
        return input(prompt)

@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)

        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    # Use conditional logic instead of exec
    if urllib_version == '2':
        import urllib2 as urllib
        http = urllib.PoolManager()
        r = http.request('GET', url)
        print(r.data)
    elif urllib_version == '3':
        import urllib3 as urllib
        http = urllib.PoolManager()
        r = http.request('GET', url)
        print(r.data)
    else:
        print("Invalid urllib version. Use '2' or '3'.")


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = safe_input("Select vulnerability: ")
    if choice == "1": 
        new_person = Person("Vickie")  
        print_nametag(safe_input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = safe_input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(safe_input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        entered_pwd = safe_input("Enter master password: ")
        authenticate(entered_pwd)

