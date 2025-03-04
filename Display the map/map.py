;==========================================
; Title: Display the map
; Author: anonymous 
;==========================================

m = folium.Map(location=[latitude_center, longitude_center], zoom_start=12)


print("Length of actual_labels:", len(actual_labels))
print("Length of predictions_array:", len(predictions_array))

# Add markers for actual labels
for i in range(0, len(actual_labels), 2):  # Iterate over the list in steps of 2
    folium.CircleMarker(
        location=[actual_labels[i], actual_labels[i+1]],  # Use each pair as latitude and longitude
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)


for i in range(0, len(predictions_array), 2):  # Iterate over the list in steps of 2
    folium.CircleMarker(
        location=[predictions_array[i], predictions_array[i+1]],  # Use each pair as latitude and longitude
        radius=5,
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(m)
