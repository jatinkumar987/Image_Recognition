import matplotlib.pyplot as plt
import matplotlib.animation as animation
import requests

api_key = 'acc_fda3db80f3e9fe9'
api_secret = '3ea945b156f77a4f749ea5b8e0d46c55'
image_url = 'https://img.freepik.com/premium-vector/angry-girl-expression_7814-545.jpg?w=2000'

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))

result = response.json()

if 'result' in result:
    tags = result['result']['tags']
    tag_names = [tag['tag']['en'] for tag in tags]
    confidence_levels = [tag['confidence'] for tag in tags]

    # Sort tags based on confidence level in descending order
    sorted_tags = sorted(zip(tag_names, confidence_levels), key=lambda x: x[1], reverse=True)
    tag_names, confidence_levels = zip(*sorted_tags)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set up the initial bar chart
    bar_chart = ax.bar(tag_names, confidence_levels)

    # Function to update the animation frame
    def update_frame(frame):
        # Update the heights of the bars with new confidence levels
        for bar, confidence in zip(bar_chart, confidence_levels):
            bar.set_height(confidence)

        # Set the title of the plot
        ax.set_title("Image Tags (Confidence Level)")

    # Create the animation
    animation = animation.FuncAnimation(fig, update_frame, frames=range(10), repeat=False)

    # Show the animated plot
    plt.show()
else:
    error_message = result['status']['text']
    print('Error:', error_message)
