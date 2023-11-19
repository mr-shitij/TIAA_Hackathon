import requests

# The URL of the API endpoint
url = 'http://localhost:3000/get_user/'

def get_user(id=1):
  # Make a GET request
  response = requests.get(url + str(id))

  # Check if the request was successful
  if response.status_code == 200:
      # Parse JSON response
      data = response.json()
      print("Response from server:", data)
  else:
      print("Error:", response.status_code)

def main():
  get_user()

if __name__ == "__main__":
	main()
