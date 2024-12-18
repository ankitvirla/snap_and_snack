# Build Your AI-Powered Nutrition Guide: Snap & Snack
Ever wondered if snapping a picture of your food could do more than just look good on Instagram? With Snap & Snack, you can turn food photography into actionable nutritional insights. This blog walks you through how we built this AI-powered nutrition guide, helping users make smarter dietary choices effortlessly.

By the end of this blog, you’ll learn how to:
- Use Flutter to create an app for food image uploads.
- Set up an API on Cloud Run to process food images using Gemini AI.
- Store nutritional data in Firestore.

## The Problem
Maintaining a healthy diet is often easier said than done. Manual food logging is tedious, and most people lack the expertise to analyze their meals’ nutritional content. This often leads to poor eating habits and an unbalanced diet. **Snap & Snack** addresses these challenges by offering an effortless way to analyze and track nutritional intake.

## The Solution
Our app leverages advanced AI to process food images and extract detailed nutritional information. By combining instant analysis with data storage and personalized insights, Snap & Snack makes it easy for users to:
- Monitor their dietary intake.
- Receive actionable recommendations for healthier eating.
- Track their progress over time

![1](https://github.com/user-attachments/assets/ee4d7fc1-47d5-45d8-af56-1075d114baf6)

## Features
1. **Instant Nutrition Analysis:** Simply snap a picture of your meal, and let our app do the rest. Using the Gemini API 2.0, Snap & Snack provides a complete nutritional breakdown, including calories, carbohydrates, fiber, vitamins, protein

![image](https://github.com/user-attachments/assets/b9fc8dee-1c79-4ae3-91a8-4089417f53dc)

2. **Effortless Logging: ** No more manual tracking! Each analysis is automatically saved in Firestore, creating a comprehensive food diary for you to reference anytime.

## Architecture Overview
![image](https://github.com/user-attachments/assets/51cdb230-55fe-4d36-85e6-af64f12abec5)

## Design
Our solution leverages:
1. **Frontend:** A Flutter-based app for image uploads.
2. **Backend:** Cloud Run to host the API and integrate Gemini AI for food analysis.
3. **Database:** Firestore to store detailed nutritional data for each meal.

## Design Choices
1. **Flutter:** Chosen for its cross-platform capabilities and rich UI components.
2. **Cloud Run:** Provides a serverless, scalable solution to host APIs.
3. **Gemini AI:** Offers advanced image analysis for extracting nutritional details.
4. **Firestore:** Ensures fast, real-time storage and retrieval of user data.

## Prerequisites
Before you start, ensure you have the following:
1. Flutter SDK installed.
2. Google Cloud SDK for deploying Cloud Run services.
3. Firestore Database with native mode enabled.
4. Google Cloud Credits: You can sign up for free credits
5. A valid API key for Gemini AI
6. Basic knowledge of Python, Flutter, and REST APIs.

## Step-by-Step Instructions
### Step 1: Create the Flutter App
1. Initialize a Flutter project:

```dart
flutter create snap_snack
cd snap_snack
```

2. Add dependencies for image access and HTTP requests:
```dart
dependencies:
  image_picker: ^0.8.5+3
  http: ^0.15.0
```

3. Grant image access permissions in AndroidManifest.xml (Android)
```dart
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.CAMERA" />
```

### Step 2: Implement the Image Upload Feature
1. Create a button to pick or capture images:
```dart
import 'package:image_picker/image_picker.dart';

final picker = ImagePicker();
final pickedFile = await picker.pickImage(source: ImageSource.gallery);
```

2. Upload the image to the Cloud Run API using the http package:
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

final response = await http.post(
  Uri.parse('<CLOUD_RUN_API_URL>'),
  headers: {"Content-Type": "application/json"},
  body: json.encode({"file": pickedFile.path}),
);
```

### Step 3: Deploy the Backend on Cloud Run

1. Prepare the backend environment:
```bash
pip install flask google-cloud-firestore google-generativeai
```

2. Implement the API in [main.py]((https://example.com/path/to/file.pdf))
3. Deploy the function to Cloud Run

### Step 4: Store Data in Firestore
1. The backend stores processed nutritional data in Firestore:
```python
doc_ref = db.collection('nutrition').document()
doc_ref.set(response)
```

### Step 5: Integrate API in Flutter App
1. Update your app to display nutritional data returned by the API:
```python
if (response.statusCode == 200) {
    final data = json.decode(response.body);
    print('Nutritional Info: $data');
}
```

## Result
1. App functionality
[Watch the video](https://youtube.com/shorts/0eLQt6zFCmY?si=j5YpzEkn5AuOzkVk)

2. Firestore db Screenshot
![image](https://github.com/user-attachments/assets/4c9415b9-0923-4ed5-b47a-56c83c5de2cb)

## Challenges Faced
**Firestore Integration:** Initially, we encountered issues while integrating Firestore with Cloud Run due to database configuration settings. Switching Firestore to native mode resolved the problem.

## Future Developments
1. **Personalized Insights:** Enhanced user-specific recommendations based on eating habits.
2. **Interactive Chatbot:** A conversational AI feature to answer users’ questions about nutritional values and recommendations.
3. **Reminder: ** For those who often fall into unhealthy eating patterns, Snap & Snack sends gentle reminders and alerts to help you stay on track.

## Conclusion
Snap & Snack bridges the gap between casual food photography and serious nutrition tracking. By combining the power of AI with user-friendly features, it empowers users to take charge of their health effortlessly.
Thanks to my teammate Swechchha.

## Connect
Reach out to me on [LinkedIn](https://www.linkedin.com/in/ankitbirla/)
Let’s make healthy eating simple and fun!

To learn more about Google Cloud services and to create an impact for the work you do, get around to these steps right away:
- Register for [Code Vipassana sessions](https://rsvp.withgoogle.com/events/cv)
- Join the meetup group [Datapreneur Social](https://www.meetup.com/datapreneur-social/)
- Sign up to become [Google Cloud Innovator](https://cloud.google.com/innovators?utm_source=cloud_sfdc&utm_medium=email&utm_campaign=FY23-1H-vipassana-innovators&utm_content=joininnovators&utm_term=-)
