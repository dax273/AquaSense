# AquaSense - Quick Setup Guide

## Prerequisites

- Android Studio (latest version)
- Java 11+ installed
- An active ThingSpeak channel with test data

## Step 1: Get Your ThingSpeak Channel ID

1. Go to [ThingSpeak.com](https://thingspeak.com)
2. Sign in or create an account
3. Navigate to your channel
4. Copy the **Channel ID** from the channel settings
   - Example: `2165243` (this is the default in our code)

## Step 2: Update Channel ID in Code

Open `app/src/main/java/com/example/aquasense/ui/DashboardActivity.kt`

Find this line (around line 22):
```kotlin
private val CHANNEL_ID = "2165243" // Replace with your channel ID
```

Replace `"2165243"` with your actual ThingSpeak Channel ID:
```kotlin
private val CHANNEL_ID = "YOUR_CHANNEL_ID_HERE"
```

## Step 3: Build the Project

1. Open project in Android Studio
2. Click **File → Sync Now** (or use Gradle sync)
3. Wait for dependencies to download (first time may take a few minutes)
4. Click **Build → Build Project** to verify everything compiles

## Step 4: Run the App

### On Emulator:
1. Click **Run → Run 'app'** (or press Shift+F10)
2. Select your emulator or Android Virtual Device
3. Wait for the app to build and install

### On Physical Device:
1. Enable Developer Mode on your Android device
2. Connect device via USB
3. Click **Run → Run 'app'**
4. Select your device from the list
5. Click **OK**

## Step 5: Test the App

1. **Welcome Screen** (2.5 seconds):
   - App name "AquaSense" centered
   - Placeholder image below
   - Auto-navigates to Dashboard

2. **Dashboard Screen**:
   - Title "AquaSense" at top
   - Loading indicator (briefly)
   - Line chart with 4 colored lines (one for each field)
   - Legend showing: Field 1, Field 2, Field 3, Field 4

## Troubleshooting

### "No data available" message
- **Cause:** ThingSpeak channel has no data or wrong Channel ID
- **Fix:** 
  1. Verify your Channel ID is correct
  2. Ensure channel has data in at least one field
  3. Check internet connection

### Build fails with "Gradle sync failed"
- **Cause:** Dependency download issues
- **Fix:**
  1. Check internet connection
  2. Click **File → Invalidate Caches → Invalidate and Restart**
  3. Try sync again

### "Cannot find symbol: ActivityWelcomeBinding"
- **Cause:** ViewBinding not generated
- **Fix:**
  1. Check `build.gradle.kts` has `viewBinding = true` in `buildFeatures`
  2. Click **Build → Clean Project**
  3. Click **Build → Rebuild Project**

### App crashes on Dashboard
- **Cause:** API request failed or JSON parsing error
- **Fix:**
  1. Check internet connectivity
  2. Verify Thunder Channel ID is valid
  3. Check logcat for detailed error message

### Chart shows no data
- **Cause:** Feed fields are null or not numbers
- **Fix:**
  1. Verify ThingSpeak channel has numeric data
  2. Check that fields 1-4 contain valid numbers
  3. Ensure at least one data point exists

## Features to Try

1. **Zoom:** Use pinch gesture on chart
2. **Pan:** Drag your finger across chart
3. **Double Tap:** Reset zoom to default
4. **Legend:** Tap legend items to show/hide lines
5. **Data Points:** Long press points for values

## Customizing Colors

To change app colors:
1. Open `app/src/main/res/values/colors.xml`
2. Modify color hex values:
   ```xml
   <color name="cream_bg">#FFF5F0E8</color>
   <color name="lime_green">#FFD4F040</color>
   ```
3. Rebuild app

To change chart line colors:
1. Open `app/src/main/java/com/example/aquasense/ui/DashboardActivity.kt`
2. Find the `LineDataSet` configurations (around lines 95-129)
3. Modify the color hex values:
   ```kotlin
   color = Color.parseColor("#YOURCOLOR")
   ```

## Common ThingSpeak API Responses

### Success Response
```json
{
  "channel": {
    "id": 123456,
    "name": "My IoT Channel",
    "description": "Sensor data"
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

### Empty Response (No Data)
```json
{
  "channel": {...},
  "feeds": []
}
```

## Performance Tips

1. **Use real device** for better performance than emulator
2. **Close other apps** to free up memory
3. **Limit data points** - currently fetches 20 points (adjust in code if needed)
4. **Check internet** - 4G/WiFi recommended for smooth experience

## Next Steps After Setup

1. **Add More Fields:**
   - Modify `ThingSpeakResponse.kt` to add field5, field6, etc.
   - Update `DashboardActivity.kt` to parse and display new fields

2. **Add Refresh Button:**
   - Add button to dashboard XML layout
   - Call `fetchAndDisplayData()` on button click

3. **Custom Branding:**
   - Replace `ic_launcher_foreground.xml` with your logo
   - Update colors in `colors.xml`

4. **Multiple Channels:**
   - Create variant activities for different channels
   - Allow user selection from dropdown menu

## Support & Debugging

For detailed information, see:
- **Architecture:** Check `README.md`
- **Code Structure:** View `ARCHITECTURE.md` (if available)
- **ThingSpeak API:** https://thingspeak.com/docs/channels
- **MPAndroidChart:** https://github.com/PhilJay/MPAndroidChart

## Android Minimum Requirements

- **Minimum SDK:** API 24 (Android 7.0)
- **Target SDK:** API 36
- **Compile SDK:** API 36
- **Java Version:** 11

## File Sizes (Approximate)

- APK Size: ~15-20 MB (with dependencies)
- Data Usage: ~5-10 KB per API call
- Memory Usage: ~100-150 MB while running

Enjoy your AquaSense IoT Dashboard! 🌟

