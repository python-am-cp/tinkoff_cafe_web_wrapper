from django.shortcuts import render
# Create your views here.
# This function will return and render the home page when url is http://localhost:8000/to_do/.
def index_page(request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    return render(request, 'index.html')