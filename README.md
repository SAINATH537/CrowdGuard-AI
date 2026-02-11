CrowdGuard - AI is a comprehensive security and surveillance web application that leverages existing CCTV networks, machine learning, and real-time analytics to detect fights and manage broadcasts across various locations. The platform provides live feeds, historical logs, advanced analytics, and role-based controls to ensure efficient monitoring and rapid response.

Features
Real-Time Fight Detection: Processes live CCTV video streams using a custom ML model with an AttentionLayer to detect fights in real time.
Live Feed Display: Presents live video streams from security cameras with real-time ML predictions (fight vs. no fight).
Historical Data Logging: Logs anomaly events and alarm history with detailed timestamps, durations, and actions taken.
Analytics Dashboard: Visualizes performance metrics and insights using Chart.js, including anomaly status distribution, trend analysis, and alarm durations.
Voice Broadcast: Allows admins to send voice messages to specific rooms by recording audio from the browser microphone.
Text Broadcast: Enables admins to send text broadcast messages to various locations.
Role-Based Access Control: Only authenticated users can view feeds, while administrative tasks such as broadcast and data management are restricted to admins.
Rate Limiting: All routes are rate limited to prevent abuse using Flask-Limiter.
Modular Architecture: Built using Flask blueprints for feed, broadcast, history, authentication, and analytics.
Data Management Scripts: Includes scripts to seed sample data and clear anomalies and alarm history.
