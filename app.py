import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # Used for consistency, though px handles pie charts well

# --- Streamlit Page Configuration ---
# Sets the page layout to wide and provides a title for the browser tab
st.set_page_config(
    layout="wide",
    page_title="Interactive Media Intelligence Dashboard",
    initial_sidebar_state="expanded" # Optional: Can be "auto", "expanded", or "collapsed"
)

# --- Custom CSS for Modern, Futuristic Look ---
# Injects custom CSS to style Streamlit components for a darker, more futuristic theme
st.markdown("""
    <style>
    /* Main container background gradient */
    .stApp {
        background: linear-gradient(to bottom right, #1a202c, #000000); /* Dark gradient */
        color: #e0e0e0; /* Light text color */
        font-family: 'Inter', sans-serif; /* Consistent font */
    }
    /* Header styling with gradient text */
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        text-align: center;
        background: -webkit-linear-gradient(left, #a855f7, #4f46e5); /* Purple to Indigo gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 8px;
        display: inline-block;
        border-radius: 8px;
    }
    .sub-header-font {
        font-size: 20px !important;
        text-align: center;
        color: #9ca3af; /* Gray text for subtitle */
    }
    /* Section headers */
    .section-header {
        font-size: 28px !important;
        font-weight: 600;
        color: #a78bfa; /* Purple for section titles */
        margin-bottom: 16px;
    }
    /* List item styling for user guide */
    .list-item {
        margin-bottom: 8px;
    }
    /* General container styling for sections and charts */
    .plotly-container {
        background-color: #1f2937; /* Darker gray background */
        border: 1px solid #374151; /* Gray border */
        border-radius: 0.75rem; /* Rounded corners */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* Shadow effect */
        padding: 24px;
        display: flex;
        flex-direction: column;
        transition: all 0.3s ease-in-out; /* Smooth transition for hover effects */
        height: 100%; /* Ensure containers fill height */
    }
    .plotly-container:hover {
        border-color: #6366f1; /* Blue border on hover */
    }
    /* Insights section title */
    .insights-title {
        font-size: 20px !important;
        font-weight: 600;
        color: #bfdbfe; /* Light blue for insights title */
        margin-top: 16px;
        margin-bottom: 8px;
    }
    /* Individual insight text */
    .insight-paragraph {
        margin-bottom: 0.5rem; /* Space between paragraphs */
        color: #d1d5db; /* Lighter gray for insight text */
        font-size: 0.875rem; /* sm text */
        line-height: 1.4;
    }
    /* Adjust Plotly chart text for dark theme */
    .plotly .modebar {
      background-color: rgba(0,0,0,0.5) !important;
      border-radius: 8px;
    }
    .plotly .modebar-btn {
      color: #E0E0E0 !important;
    }
    .plotly .modebar-btn:hover {
      background-color: rgba(255,255,255,0.1) !important;
    }
    .plotly .gtitle {
      font-family: 'Inter', sans-serif !important;
      color: #E0E0E0 !important;
    }
    .plotly .gbox, .plotly .gtext {
      fill: #E0E0E0 !important;
      font-family: 'Inter', sans-serif !important;
    }
    .plotly .xtick, .plotly .ytick {
      fill: #9CA3AF !important; /* light gray for ticks */
    }
    .plotly .axis-title {
      fill: #C0C0C0 !important; /* slightly darker gray for axis titles */
    }
    /* Custom scrollbar for dark theme */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #2D3748; /* Dark gray */
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #4A5568; /* Slightly lighter gray */
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #6B7280; /* Even lighter gray on hover */
    }
    </style>
""", unsafe_allow_html=True) # Allows Streamlit to render raw HTML and CSS

# --- Header Section ---
# Uses st.markdown with unsafe_allow_html=True to embed custom HTML for the main title and subtitle
st.markdown("""
    <div style="text-align: center; margin-bottom: 32px;">
        <h1 class="big-font">Interactive Media Intelligence Dashboard</h1>
        <p class="sub-header-font">Gain insights from your media data</p>
    </div>
""", unsafe_allow_html=True)

# --- User Guide Section ---
st.markdown("---") # Horizontal line separator
st.markdown("""
<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563;">
    <h2 class="section-header" style="color: #6ee7b7;">How to Use This Dashboard</h2>
    <p class="text-gray-300 leading-relaxed mb-4">
        Follow these simple steps to analyze your media data:
    </p>
    <ol class="list-decimal list-inside text-gray-300 space-y-2 ml-4">
        <li class="list-item">
            <span class="font-semibold" style="color: #d8b4fe;">Prepare your CSV file:</span> Ensure it has the following columns: <code style="background-color: #374151; border-radius: 0.25rem; padding: 0.25rem 0.5rem; font-size: 0.875rem;">Date</code>, <code style="background-color: #374151; border-radius: 0.25rem; padding: 0.25rem 0.5rem; font-size: 0.875rem;">Platform</code>, <code style="background-color: #374151; border-radius: 0.25rem; padding: 0.25rem 0.5rem; font-size: 0.875rem;">Sentiment</code>, <code style="background-color: #374151; border-radius: 0.25rem; padding: 0.25rem 0.5rem; font-size: 0.875rem;">Location</code>, <code style="background-color: #374151; border-radius: 0.25rem; padding: 0.25rem 0.5rem; font-size: 0.875rem;">Engagements</code>, <code style="background-color: #374151; border-radius: 0.25rem; padding: 0.25rem 0.5rem; font-size: 0.875rem;">Media Type</code>.
        </li>
        <li class="list-item">
            <span class="font-semibold" style="color: #d8b4fe;">Upload your CSV:</span> Use the file uploader below to select your prepared CSV.
        </li>
        <li class="list-item">
            <span class="font-semibold" style="color: #d8b4fe;">View the insights:</span> Once uploaded, the dashboard will automatically clean your data and display interactive charts along with key insights for each visualization.
        </li>
    </ol>
</div>
""", unsafe_allow_html=True)

# --- File Upload Section ---
st.markdown("---")
# Custom container for the file uploader section
st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563;">'
            '<h2 class="section-header" style="color: #d8b4fe;">1. Upload Your CSV File</h2>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type="csv") # Streamlit's file uploader widget
st.markdown('</div>', unsafe_allow_html=True)

df = None # Initialize DataFrame to None

if uploaded_file is not None:
    # --- Data Cleaning Process ---
    st.markdown("---")
    # Custom container for the data cleaning section
    st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563;">'
                '<h2 class="section-header" style="color: #d8b4fe;">2. Data Cleaning Process</h2>'
                '<p class="text-gray-300 leading-relaxed">'
                'The dashboard automatically performs the following data cleaning steps upon CSV upload:'
                '</p>'
                '<ul class="list-disc list-inside text-gray-400 mt-2 ml-4">'
                '<li>Converts the \'Date\' column to a proper datetime format.</li>'
                '<li>Fills any missing values in the \'Engagements\' column with a default of 0.</li>'
                '<li>Normalizes column names (e.g., `Date` becomes `date`, `Media Type` becomes `mediatype`) for consistent processing.</li>'
                '<li>Rows with invalid or unparseable dates will be filtered out.</li>'
                '</ul>', unsafe_allow_html=True)
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Normalize column names: strip whitespace, convert to lowercase, replace spaces with empty string
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '')

        # Convert 'Date' column to datetime objects
        # errors='coerce' will convert parsing errors into NaT (Not a Time)
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        # Drop rows where 'date' is NaT (i.e., invalid dates)
        df.dropna(subset=['date'], inplace=True)

        # Fill missing 'Engagements' with 0 and ensure float type
        df['engagements'] = df['engagements'].fillna(0).astype(float)

        # Display success message after cleaning
        st.markdown(f'<p class="text-green-400 mt-4 text-center">Data cleaned successfully! Showing {len(df)} valid entries.</p>', unsafe_allow_html=True)

    except Exception as e:
        # Display error message if file processing fails
        st.markdown(f'<p class="text-red-400 mt-4 text-center">Error processing file: {e}</p>', unsafe_allow_html=True)
        df = None # Reset df to None to prevent chart generation on error
    st.markdown('</div>', unsafe_allow_html=True) # Close the data cleaning container

# --- Chart Generation and Insights Display ---
if df is not None and not df.empty:
    st.markdown("---")
    # Section header for charts
    st.markdown('<h2 class="section-header" style="color: #a78bfa;">Interactive Charts</h2>', unsafe_allow_html=True)

    # Helper function to render insights
    def render_insights(insights):
        for insight in insights:
            st.markdown(f'<p class="insight-paragraph">{insight}</p>', unsafe_allow_html=True)

    # --- Insight Generation Functions ---
    # These functions calculate and return a list of textual insights based on chart data
    def get_sentiment_insights(sentiment_counts):
        total = sum(sentiment_counts.values())
        sorted_sentiments = sorted(sentiment_counts.items(), key=lambda item: item[1], reverse=True)
        insights = []
        insights.append(f"This chart describes the distribution of sentiment (positive/negative/neutral) towards a brand, campaign, or topic, providing a quick snapshot of public perception.")
        if len(sorted_sentiments) > 0:
            insights.append(f"1. The dominant sentiment is \"{sorted_sentiments[0][0]}\" accounting for {((sorted_sentiments[0][1] / total) * 100):.1f}% of all entries. This indicates the primary public opinion.")
        if len(sorted_sentiments) > 1:
            insights.append(f"2. \"{sorted_sentiments[1][0]}\" is the second most common sentiment, showing varied public opinion.")
        if len(sorted_sentiments) > 2:
            insights.append(f"3. Understanding the sentiment distribution is crucial for crafting effective communication strategies.")
        
        # Consolidated Recommendation
        insights.append(f"Recommendation: If dominant sentiment is negative, develop a crisis communication plan. If positive, amplify successful content. If neutral, engage to convert to positive advocates.")
        return insights

    def get_engagement_trend_insights(dates, engagements):
        insights = []
        if len(dates) == 0: return insights
        insights.append(f"This chart shows fluctuations in content engagement over time, ideal for tracking media campaign performance and identifying peaks or declines. It provides a dynamic view of audience interaction.")

        max_engagement = max(engagements)
        min_engagement = min(engagements)
        # Find index and get corresponding date, format as string
        max_date_str = dates[engagements.index(max_engagement)].strftime('%Y-%m-%d')
        min_date_str = dates[engagements.index(min_engagement)].strftime('%Y-%m-%d')


        insights.append(f"1. Peak engagement occurred around {max_date_str}, reaching {max_engagement:,.0f} total engagements. Analyze this date to identify triggers for the surge.")
        insights.append(f"2. The lowest engagement period was around {min_date_str}, with only {min_engagement:,.0f} engagements. Investigate this decline to prevent similar issues.")

        first_half_engagements = sum(engagements[:len(engagements) // 2])
        second_half_engagements = sum(engagements[len(engagements) // 2:])

        if second_half_engagements > first_half_engagements:
            insights.append('3. Engagement trends show an increase in the latter half, indicating positive results from your content strategy.')
        elif second_half_engagements < first_half_engagements:
            insights.append('3. A decline in engagement is observed in the latter half, suggesting deeper analysis into content performance is needed.')
        else:
            insights.append('3. Engagement levels remained relatively stable, indicating consistent audience interaction.')
        
        # Consolidated Recommendation
        insights.append(f"Recommendation: Replicate successful content strategies during peak periods. Analyze content from low engagement periods to identify weaknesses and adjust your content calendar. Continue current strategies for growth, or explore new tactics to break stagnation.")
        return insights

    def get_platform_insights(platform_engagements):
        sorted_platforms = sorted(platform_engagements.items(), key=lambda item: item[1], reverse=True)
        insights = []
        insights.append(f"This chart compares engagement performance across social media platforms or news portals, helping to identify the most effective platforms for reach and interaction. This is crucial for optimizing resource allocation.")
        if len(sorted_platforms) > 0:
            insights.append(f"1. \"{sorted_platforms[0][0]}\" is the leading platform, generating {sorted_platforms[0][1]:,.0f} engagements. This highlights your most effective channel.")
        if len(sorted_platforms) > 1:
            insights.append(f"2. \"{sorted_platforms[1][0]}\" also shows strong performance with {sorted_platforms[1][1]:,.0f} engagements, indicating significant potential for diversification.")
        insights.append('3. Disparities in engagement across platforms emphasize the importance of strategically allocating resources for the highest engagement ROI.')
        
        # Consolidated Recommendation
        insights.append(f"Recommendation: Allocate more budget/resources to leading platforms and analyze successful content types for cross-platform adaptation. Consider reducing investment in underperforming platforms or re-evaluating their role in your overall media strategy.")
        return insights

    def get_media_type_insights(media_type_counts):
        total = sum(media_type_counts.values())
        sorted_media_types = sorted(media_type_counts.items(), key=lambda item: item[1], reverse=True)
        insights = []
        insights.append(f"This chart analyzes the proportion of media types, providing insight into your audience's most preferred content formats. This is key for an audience-centric content strategy.")
        if len(sorted_media_types) > 0:
            insights.append(f"1. \"{sorted_media_types[0][0]}\" is the most frequently used media type, accounting for {((sorted_media_types[0][1] / total) * 100):.1f}% of content. This indicates a clear audience preference.")
        if len(sorted_media_types) > 1:
            insights.append(f"2. \"{sorted_media_types[1][0]}\" is the second most common, indicating audiences also respond well to this format.")
        insights.append('3. Analyzing engagement rates per media type is crucial for optimizing content strategy and discovering new opportunities.')
        
        # Consolidated Recommendation
        insights.append(f"Recommendation: Prioritize creating more content in preferred formats. Maintain a healthy mix of content by continuing to produce other media types, and explore ways to enhance their impact. Experiment with converting high-performing content between formats.")
        return insights

    def get_location_insights(sorted_locations):
        insights = []
        insights.append(f"This chart identifies geographical locations with the highest total engagement, relevant for audience targeting or localized content production. This helps inform regional marketing decisions.")
        if len(sorted_locations) > 0:
            insights.append(f"1. The top location for engagements is \"{sorted_locations[0][0]}\" with {sorted_locations[0][1]:,.0f} total engagements. This indicates audiences in this region are highly active.")
        if len(sorted_locations) > 1:
            insights.append(f"2. \"{sorted_locations[1][0]}\" is the second highest, indicating key geographical areas for focus.")
        insights.append('3. Knowing high-engagement locations allows you to design more targeted marketing campaigns or develop culturally relevant content.')
        
        # Consolidated Recommendation
        insights.append(f"Recommendation: Launch localized campaigns, run geo-targeted ads, or create region-specific content to deepen engagement in top locations. Explore expanding your presence or tailoring content for secondary high-engagement locations.")
        return insights

    # --- Chart 1: Sentiment Breakdown (Pie Chart) ---
    col1, col2 = st.columns(2) # Create two columns for charts

    with col1:
        st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563; margin-bottom: 32px;">'
                    '<h2 class="section-header" style="color: #93c5fd;">3.1. Sentiment Breakdown (Pie Chart)</h2>', unsafe_allow_html=True)
        sentiment_counts = df['sentiment'].value_counts()
        fig_sentiment = px.pie(
            names=sentiment_counts.index,
            values=sentiment_counts.values,
            hole=0.4,
            title='Sentiment Breakdown',
            color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#FFA15A', '#19D3F3']
        )
        # Update layout for dark theme
        fig_sentiment.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E0E0E0', family='Inter, sans-serif'),
            legend=dict(font=dict(color='#E0E0E0')),
            height=400, # Fixed height for consistency
            margin=dict(l=20, r=20, b=20, t=60) # Adjust margins
        )
        st.plotly_chart(fig_sentiment, use_container_width=True) # Display chart in Streamlit
        st.markdown('<h3 class="insights-title" style="color: #bfdbfe;">Top 3 Insights:</h3>', unsafe_allow_html=True)
        render_insights(get_sentiment_insights(sentiment_counts.to_dict()))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # --- Chart 2: Engagement Trend over Time (Line Chart) ---
        st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563; margin-bottom: 32px;">'
                    '<h2 class="section-header" style="color: #6ee7b7;">3.2. Engagement Trend Over Time (Line Chart)</h2>', unsafe_allow_html=True)
        # Resample data to daily frequency and sum engagements for trend analysis
        daily_engagements = df.set_index('date').resample('D')['engagements'].sum().reset_index()
        fig_engagement_trend = px.line(
            daily_engagements,
            x='date',
            y='engagements',
            title='Engagement Trend Over Time',
            markers=True,
            line_shape='linear',
            color_discrete_sequence=['#636EFA']
        )
        fig_engagement_trend.update_layout(
            xaxis_title='Date',
            yaxis_title='Total Engagements',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E0E0E0', family='Inter, sans-serif'),
            xaxis=dict(gridcolor='#444'), # Customize grid color
            yaxis=dict(gridcolor='#444'),
            height=400, # Fixed height
            margin=dict(l=60, r=20, b=60, t=60) # Adjust margins
        )
        st.plotly_chart(fig_engagement_trend, use_container_width=True)
        st.markdown('<h3 class="insights-title" style="color: #d1fae5;">Top 3 Insights:</h3>', unsafe_allow_html=True)
        # Ensure dates are in a format compatible with insight function (e.g., datetime objects or strings)
        render_insights(get_engagement_trend_insights(daily_engagements['date'].tolist(), daily_engagements['engagements'].tolist()))
        st.markdown('</div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2) # Create new columns for the next set of charts

    with col3:
        # --- Chart 3: Platform Engagements (Bar Chart) ---
        st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563; margin-bottom: 32px;">'
                    '<h2 class="section-header" style="color: #f87171;">3.3. Platform Engagements (Bar Chart)</h2>', unsafe_allow_html=True)
        platform_engagements = df.groupby('platform')['engagements'].sum().reset_index()
        fig_platform = px.bar(
            platform_engagements,
            x='platform',
            y='engagements',
            title='Platform Engagements',
            color_discrete_sequence=['#EF553B']
        )
        fig_platform.update_layout(
            xaxis_title='Platform',
            yaxis_title='Total Engagements',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E0E0E0', family='Inter, sans-serif'),
            xaxis=dict(gridcolor='#444'),
            yaxis=dict(gridcolor='#444'),
            height=400, # Fixed height
            margin=dict(l=60, r=20, b=60, t=60) # Adjust margins
        )
        st.plotly_chart(fig_platform, use_container_width=True)
        st.markdown('<h3 class="insights-title" style="color: #fca5a5;">Top 3 Insights:</h3>', unsafe_allow_html=True)
        render_insights(get_platform_insights(platform_engagements.set_index('platform')['engagements'].to_dict()))
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        # --- Chart 4: Media Type Mix (Pie Chart) ---
        st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563; margin-bottom: 32px;">'
                    '<h2 class="section-header" style="color: #fcd34d;">3.4. Media Type Mix (Pie Chart)</h2>', unsafe_allow_html=True)
        media_type_counts = df['mediatype'].value_counts()
        fig_media_type = px.pie(
            names=media_type_counts.index,
            values=media_type_counts.values,
            hole=0.4,
            title='Media Type Mix',
            color_discrete_sequence=['#00CC96', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']
        )
        fig_media_type.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E0E0E0', family='Inter, sans-serif'),
            legend=dict(font=dict(color='#E0E0E0')),
            height=400, # Fixed height
            margin=dict(l=20, r=20, b=20, t=60) # Adjust margins
        )
        st.plotly_chart(fig_media_type, use_container_width=True)
        st.markdown('<h3 class="insights-title" style="color: #fde68a;">Top 3 Insights:</h3>', unsafe_allow_html=True)
        render_insights(get_media_type_insights(media_type_counts.to_dict()))
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Chart 5: Top 5 Locations (Bar Chart) ---
    # This chart spans full width, so it's not placed in a column with others
    st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563; margin-bottom: 32px;">'
                '<h2 class="section-header" style="color: #a78bfa;">3.5. Top 5 Locations by Engagements (Bar Chart)</h2>', unsafe_allow_html=True)
    # Group by location, sum engagements, get top 5, and reset index for Plotly
    location_engagements = df.groupby('location')['engagements'].sum().nlargest(5).reset_index()
    fig_location = px.bar(
        location_engagements,
        x='location',
        y='engagements',
        title='Top 5 Locations by Engagements',
        color_discrete_sequence=['#FFA15A']
    )
    fig_location.update_layout(
        xaxis_title='Location',
        yaxis_title='Total Engagements',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E0E0E0', family='Inter, sans-serif'),
        xaxis=dict(gridcolor='#444'),
        yaxis=dict(gridcolor='#444'),
        height=400, # Fixed height
        margin=dict(l=60, r=20, b=60, t=60) # Adjust margins
    )
    st.plotly_chart(fig_location, use_container_width=True)
    st.markdown('<h3 class="insights-title" style="color: #d8b4fe;">Top 3 Insights:</h3>', unsafe_allow_html=True)
    # Convert DataFrame to a list of lists for insight function
    render_insights(get_location_insights(location_engagements.values.tolist()))
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Concluding Recommendations Section ---
    st.markdown("---")
    st.markdown('<div class="plotly-container" style="background-color: #1f2937; border-color: #4b5563; margin-top: 32px;">'
                '<h2 class="section-header" style="color: #6ee7b7;">4. Concluding Recommendations</h2>'
                '<p class="insight-paragraph">'
                'Based on the analyzed media intelligence data, here are some overarching recommendations to optimize your strategy:'
                '</p>'
                '<ul class="list-disc list-inside text-gray-300 space-y-2 ml-4">'
                '<li class="insight-paragraph">'
                'Focus on High-Performing Channels & Content: Prioritize your efforts on platforms and media types that consistently show higher engagement. Allocate resources where your audience is most responsive.'
                '</li>'
                '<li class="insight-paragraph">'
                'Address Sentiment Gaps: If negative sentiment is significant, develop targeted strategies for reputation management. For neutral sentiment, consider engaging content to foster stronger positive connections.'
                '</li>'
                '<li class="insight-paragraph">'
                'Capitalize on Engagement Peaks & Learn from Dips: Use historical engagement trends to plan future content releases or campaign launches around peak times. Analyze factors contributing to dips to refine future strategies.'
                '</li>'
                '<li class="insight-paragraph">'
                'Tailor Content to Key Locations: Leverage insights from top-performing locations to create localized campaigns, content, or product offerings that resonate deeply with regional audiences.'
                '</li>'
                '<li class="insight-paragraph">'
                'Continuous Monitoring & Adaptation: Media landscapes evolve rapidly. Continuously monitor these metrics and be prepared to adapt your strategies based on emerging trends and audience feedback.'
                '</li>'
                '</ul>'
                '</div>', unsafe_allow_html=True)
