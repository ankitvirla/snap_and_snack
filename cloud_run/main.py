import functions_framework
import requests
from flask import jsonify
import base64
import google.generativeai as genai
from google.cloud import firestore
genai.configure(api_key="<your gemini api key>")
model = genai.GenerativeModel(model_name = "gemini-2.0-flash-exp")
db = firestore.Client()

@functions_framework.http
def hello_http(request):
    """
    HTTP Cloud Function to process an image and call the Gemini API.
    
    Args:
        request (flask.Request): The request object.
        
    Returns:
        Response object with the API response or error message.
    """
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    try:
        # Read the image content
        image_content = file.read()
        image_base64 = base64.b64encode(image_content).decode('utf-8')

        
        # Call Gemini API
        #gemini_api_url = "https://gemini-api.example.com/endpoint"  # Replace with actual Gemini API URL
        #headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Add authentication if required
        prompt = "detect all the possible ingrediets used in making this dish. once that is done provide me a list of some generic nutitional labels for those ingredients. always make assuptions if unknown. only return the response in a json in the following json format. {\"extra_response\":<other extra response content>,\"calories\":<value in string>, \"carbs\":\"<value in string>\",\"protient\":\"<value in string>\", \"vitamins\":\"list of vitamins\",\"fibre\":\"<value in string>\",\"serving\":<serving in string>}."
        response = model.generate_content([{'mime_type':'image/jpeg', 'data':image_base64}, prompt])

        #files = {'image': image_content}  # Pass the image as a file
        #response = requests.post(gemini_api_url, headers=headers, files=files)
        
        if response:
            try:
                response = response.text
                response = response.replace("```json","")
                response = response.replace("```","")
                response = eval(response)
                doc_ref = db.collection('nutrition').document()  # Auto-generate document ID
                doc_ref.set(response)
                return response, 200
            except Exception as e:
                print(e)
                return response, 200
        else:
            return jsonify({"error": "Failed to process image via Gemini API", 
                            "details": response.text}), response.status_code
    
    except Exception as e:
        return jsonify({"error": "An error occurred while processing the image",
                        "details": str(e)}), 500
