# v1.0 - Android IoT Dashboard App

## Project Overview

AquaSense is a complete Android application built in Kotlin that displays IoT sensor data from ThingSpeak in real-time using a line chart visualization.

## Features

### 1. Welcome Screen (Splash Screen)
- Displays the app name "AquaSense" centered on screen
- Shows a placeholder image (can be replaced with custom logo)
- Automatically navigates to Dashboard after 3.0 seconds
- Modern UI styling with cream background and custom colors

### 2. Dashboard Screen
- Displays app title at the top
- Shows a real-time line chart with 4 data streams
- Plots field1, field2, field3, field4 from ThingSpeak API
- Each field has a distinct color for easy visualization
- Interactive chart with zoom and pan capabilities
- Progress indicator while loading data
- Error handling with user feedback

## Application Architecture

### Layers

**Data Layer** (`com.example.aquasense.data`)
- `api/` - Retrofit API clients and interfaces
  - `ThingSpeakApi.kt` - Retrofit interface for ThingSpeak API
  - `RetrofitClient.kt` - Retrofit instance and configuration
- `model/` - Data classes
  - `ThingSpeakResponse.kt` - Parses ThingSpeak JSON response

**UI Layer** (`com.example.aquasense.ui`)
- `WelcomeActivity.kt` - Splash screen with auto-navigation
- `DashboardActivity.kt` - Main dashboard with line chart

### Resources
- `res/layout/` - XML layout files
  - `activity_welcome.xml` - Welcome screen layout
  - `activity_dashboard.xml` - Dashboard screen layout
- `res/values/` - Colors and themes
  - `colors.xml` - Custom color palette
  - `themes.xml` - App theme styling

## Technical Stack

### Dependencies
- **Retrofit 2.9.0** - HTTP client for API calls
- **Gson** - JSON serialization/deserialization
- **Kotlin Coroutines** - Asynchronous operations
- **MPAndroidChart 3.1.0** - Line chart visualization
- **Android Lifecycle** - Lifecycle-aware coroutines

### Kotlin Features Used
- Coroutines with `lifecycleScope.launch` for network calls
- Data classes for type-safe JSON parsing
- Extension functions for null safety
- Apply blocks for object configuration

## Configuration

### ThingSpeak API

**Base URL:** `https://api.thingspeak.com/`

**Endpoint:** `/channels/{CHANNEL_ID}/feeds.json?results=20`

**Important:** Update the `CHANNEL_ID` in `DashboardActivity.kt` with your actual ThingSpeak channel ID:

```kotlin
private val CHANNEL_ID = "xxxxxxx" // Replace with your channel ID
```

### Build Dependencies (libs.versions.toml)

All required libraries are defined in `gradle/libs.versions.toml`:
- Retrofit and Gson for API communication
- Coroutines for async operations
- MPAndroidChart for data visualization
- Lifecycle components for lifecycle-aware operations

## Data Flow

1. **App Launch** → WelcomeActivity displays splash screen
2. **After 2.5 seconds** → Navigate to DashboardActivity
3. **Dashboard Load** → Issue network request to ThingSpeak API via Retrofit
4. **Parse Response** → Deserialize JSON to Kotlin data classes
5. **Prepare Chart Data** → Convert feeds to Entry objects for each field
6. **Render Chart** → Display 4-line chart with legend
7. **User Interaction** → Pan, zoom, and explore chart data

## Color Scheme

Based on reference UI design:
- **Background (Cream):** #F5F0E8
- **Primary (Lime Green):** #D4F040
- **Secondary (Light Blue):** #B3E5FC
- **Dark Text:** #2C2C2C
- **Light Text:** #666666

### Chart Line Colors
- **Field 1:** Lime Green (#D4F040)
- **Field 2:** Deep Orange (#FF5722)
- **Field 3:** Blue (#2196F3)
- **Field 4:** Purple (#9C27B0)

## Permissions Required

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

## Error Handling

The app gracefully handles:
- Network errors with toast notifications
- Empty API responses
- Null field values (defaults to 0f)
- Parse exceptions with user-friendly error messages

## Customization

### Change ThingSpeak Channel
Edit `DashboardActivity.kt`:
```kotlin
private val CHANNEL_ID = "YOUR_CHANNEL_ID"
```

### Modify Chart Colors
Edit the `LineDataSet` configurations in `DashboardActivity.kt`:
```kotlin
val lineDataSet1 = LineDataSet(entries1, "Field 1").apply {
    color = Color.parseColor("#YOUR_COLOR_HEX")
    // ... other settings
}
```

### Change Chart Behavior
Modify `setupChart()` in `DashboardActivity.kt`:
- `chart.isDragEnabled = true` - Enable/disable dragging
- `chart.isScaleXEnabled = true` - Enable/disable X-axis zoom
- `chart.legend.isEnabled = true` - Show/hide legend

## UI Styling

### Theme (Light Mode)
- Background: Cream (#F5F0E8)
- Primary Color: Lime Green (#D4F040)
- Uses Material Design components with rounded corners
- Modern spacing and typography

### Theme (Night Mode)
- Same color scheme (light theme optimized for consistency)
- Defined in `values-night/themes.xml`

## Testing

The app includes placeholder test files:
- `ExampleUnitTest.kt` - Unit test placeholder
- `ExampleInstrumentedTest.kt` - Instrumented test placeholder

## Build & Run

1. Open project in Android Studio
2. Sync Gradle files
3. Set your ThingSpeak Channel ID in `DashboardActivity.kt`
4. Run on emulator or physical device (API 24+)

## File Structure

```
AquaSense2/
├── app/
│   ├── build.gradle.kts
│   ├── src/
│   │   ├── main/
│   │   │   ├── AndroidManifest.xml
│   │   │   ├── java/com/example/aquasense/
│   │   │   │   ├── data/
│   │   │   │   │   ├── api/
│   │   │   │   │   │   ├── ThingSpeakApi.kt
│   │   │   │   │   │   └── RetrofitClient.kt
│   │   │   │   │   └── model/
│   │   │   │   │       └── ThingSpeakResponse.kt
│   │   │   │   └── ui/
│   │   │   │       ├── WelcomeActivity.kt
│   │   │   │       └── DashboardActivity.kt
│   │   │   └── res/
│   │   │       ├── layout/
│   │   │       │   ├── activity_welcome.xml
│   │   │       │   └── activity_dashboard.xml
│   │   │       ├── values/
│   │   │       │   ├── colors.xml
│   │   │       │   ├── strings.xml
│   │   │       │   └── themes.xml
│   │   │       └── values-night/
│   │   │           └── themes.xml
│   │   └── test/
│   └── proguard-rules.pro
├── gradle/
│   ├── libs.versions.toml
│   └── wrapper/
├── build.gradle.kts
├── settings.gradle.kts
└── README.md
```

## Performance Considerations

- **Coroutines:** Async network calls prevent UI blocking
- **LifecycleScope:** Automatic cleanup prevents memory leaks
- **Retrofit:** Efficient HTTP caching and connection pooling
- **Chart:** Optimized rendering for smooth 4-line visualization

## API Response Format (ThingSpeak)

Expected JSON structure:
```json
{
  "channel": {
    "id": 123456,
    "name": "Channel Name",
    "description": "Description"
  },
  "feeds": [
    {
      "created_at": "2024-01-01T12:00:00Z",
      "entry_id": 1,
      "field1": "25.5",
      "field2": "60.2",
      "field3": "1013.25",
      "field4": "45.8"
    }
  ]
}
```

## Notes

- The app fetches the last 20 data points from ThingSpeak
- Data is displayed in chronological order (oldest to newest)
- Null field values are safely handled with 0f fallback
- Chart automatically reverses data array for proper time series display
- ViewBinding is used for type-safe view access
- No-argument constructor in data classes (not required for Gson)

## Future Enhancements

- Multi-channel support
- Data refresh interval configuration
- Custom field labeling
- Export chart as image
- Offline data caching
- Real-time WebSocket updates
- Data filtering and date range selection

