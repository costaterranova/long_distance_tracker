import streamlit as st
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the timeline start and end dates
start_date = datetime.date(2024, 9, 24)
end_date = datetime.date(2025, 7, 1)
today = datetime.date.today()

# Define event date ranges
event1_start = datetime.date(2024, 12, 1)
event1_end = datetime.date(2024, 12, 6)
event2_start = datetime.date(2025, 3, 1)
event2_end = datetime.date(2025, 3, 16)
event3_start = datetime.date(2025, 6, 1)
event3_end = datetime.date(2025, 6, 4)
event4_date = datetime.date(2025, 7, 1)

# Calculate progress
elapsed_days = (today - start_date).days
total_days = (end_date - start_date).days
progress = np.clip(elapsed_days / total_days, 0, 1)  # Ensure within 0-1

days_until_event3 = (event3_start - today).days
if days_until_event3 < 0:
    days_until_event3 = 0

st.title("🌸 Long Distance Progress Bar 💕")

# Matplotlib with Seaborn for a softer aesthetic
sns.set_style("white")
fig, ax = plt.subplots(figsize=(8, 1.5))

# Define event progress ranges
event1_start_progress = np.clip((event1_start - start_date).days / total_days, 0, 1)
event1_end_progress = np.clip((event1_end - start_date).days / total_days, 0, 1)
event2_start_progress = np.clip((event2_start - start_date).days / total_days, 0, 1)
event2_end_progress = np.clip((event2_end - start_date).days / total_days, 0, 1)
event3_start_progress = np.clip((event3_start - start_date).days / total_days, 0, 1)
event3_end_progress = np.clip((event3_end - start_date).days / total_days, 0, 1)
event4_progress = np.clip((event4_date - start_date).days / total_days, 0, 1)

# Draw main timeline with event sections highlighted
ax.plot([0, event1_start_progress], [0, 0], color='black', linewidth=4, alpha=0.8, linestyle='dotted')
ax.plot([event1_start_progress, event1_end_progress], [0, 0], color='red', linewidth=4, alpha=0.9)
ax.plot([event1_end_progress, event2_start_progress], [0, 0], color='black', linewidth=4, alpha=0.8, linestyle='dotted')
ax.plot([event2_start_progress, event2_end_progress], [0, 0], color='red', linewidth=4, alpha=0.9)
ax.plot([event2_end_progress, event3_start_progress], [0, 0], color='black', linewidth=4, alpha=0.8, linestyle='dotted')
ax.plot([event3_start_progress, event3_end_progress], [0, 0], color='red', linewidth=4, alpha=0.9)
ax.plot([event3_end_progress, event4_progress], [0, 0], color='black', linewidth=4, alpha=0.8, linestyle='dotted')
ax.plot([event4_progress, 1], [0, 0], color='black', linewidth=4, alpha=0.8, linestyle='dotted')

# Add today marker
ax.scatter([progress], [0], color='red', s=120, edgecolors='pink', linewidth=2, label='Today', alpha=0.9)

# Add cute vignette texts with hearts
event1_text_x = (event1_start_progress + event1_end_progress) / 2
ax.text(event1_text_x, 0.15, "\U0001F497 Nana & Costa met in Tokyo 💖", 
        fontsize=12, color='red', ha='center', fontweight='bold', 
        bbox=dict(facecolor='mistyrose', alpha=0.6, edgecolor='red', boxstyle='round,pad=0.3'))

event2_text_x = (event2_start_progress + event2_end_progress) / 2
ax.text(event2_text_x, -0.15, "🌸 Spring trip together! 🌸", 
        fontsize=12, color='red', ha='center', fontweight='bold', 
        bbox=dict(facecolor='lightpink', alpha=0.6, edgecolor='red', boxstyle='round,pad=0.3'))

event3_text_x = (event3_start_progress + event3_end_progress) / 2
ax.text(event3_text_x, 0.15, f"💞 In {days_until_event3} days, Nana & Costa will meet in NY! 💞", 
        fontsize=12, color='red', ha='center', fontweight='bold', 
        bbox=dict(facecolor='lavenderblush', alpha=0.6, edgecolor='red', boxstyle='round,pad=0.3'))

# Final event in Tokyo as a smaller purple circle
ax.scatter([event4_progress], [0], color='purple', s=150, alpha=0.8)

ax.set_xlim(0, 1)
ax.set_ylim(-0.3, 0.3)
ax.axis('off')

# Display the chart
st.pyplot(fig)

# Show textual progress with emojis
st.write(f"### ⏳ {elapsed_days} days elapsed out of {total_days} days")
st.write(f"### ⏳ In {total_days - elapsed_days} we will be together")
st.write(f"### 📍 Progress: {progress * 100:.2f}%")

with st.expander("Last trip together"):
    st.video("Video/video.mov")