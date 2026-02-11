# 🧠 Neural Nexus Dashboard

> AI-Powered Real-Time Surveillance & Security Intelligence Platform

Neural Nexus Dashboard is a production-grade security and surveillance web application that leverages existing CCTV infrastructure, machine learning, and real-time analytics to detect violent activity and manage emergency broadcasts across distributed locations.

The system provides live monitoring, anomaly detection, historical logging, advanced analytics, and secure role-based access control — enabling rapid incident response and operational efficiency.

---

# 🚀 Core Features

## 🔍 Real-Time Fight Detection
- Processes live CCTV streams using a custom ML model with AttentionLayer
- Real-time classification: Fight vs No Fight
- Low-latency prediction pipeline

## 📹 Live Feed Monitoring
- Multi-camera live feed display
- Overlayed ML predictions
- Authenticated user access only

## 🗂 Historical Event Logging
- Stores anomaly events and alarm history
- Timestamped records
- Duration tracking
- Action audit logs

## 📊 Analytics Dashboard
- Built with Chart.js
- Anomaly distribution charts
- Trend analysis over time
- Alarm duration insights

## 🔊 Voice Broadcast
- Browser-based microphone recording
- Room-specific audio broadcast
- Admin-only access

## 💬 Text Broadcast
- Real-time text alerts
- Multi-location distribution
- Admin-controlled messaging

## 🔐 Role-Based Access Control
- Authenticated user access for feeds
- Admin-only broadcast & data management
- Secure session management

## ⚡ Rate Limiting
- API and route rate limiting to prevent abuse
- Configurable request thresholds

## 🧩 Modular Architecture
- Django apps for:
  - feed
  - broadcast
  - history
  - analytics
  - authentication
  - ml_model

---

# 🏗 Production Setup Guide

## 1️ Clone Repository

```bash
git clone https://github.com/yourusername/neural-nexus-dashboard.git
cd neural-nexus-dashboard

