import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for Trends in Hackathon Participation
years = ['2018', '2019', '2020', '2021', '2022']
participants = [1200, 1500, 1800, 2200, 2500]  # Hypothetical number of participants

participation_df = pd.DataFrame({'Year': years, 'Participants': participants})

# Sample data for Types of Projects Developed
project_types = ['AI & Machine Learning', 'Web Development', 'Mobile Apps', 'Data Science', 'Blockchain']
projects_count = [200, 300, 250, 150, 100]  # Hypothetical counts

projects_df = pd.DataFrame({'Project Type': project_types, 'Count': projects_count})

# Sample data for Impact on Career Development
career_impact_categories = ['Internships Secured', 'Job Offers', 'Skill Enhancement', 'Networking Opportunities']
impact_values = [300, 200, 400, 350]  # Hypothetical numbers

career_impact_df = pd.DataFrame({'Impact Category': career_impact_categories, 'Value': impact_values})

# Creating the visualizations
plt.figure(figsize=(18, 6))

# Trends in Hackathon Participation
plt.subplot(1, 3, 1)
sns.lineplot(data=participation_df, x='Year', y='Participants', marker='o')
plt.title('Trends in Hackathon Participation')
plt.xlabel('Year')
plt.ylabel('Number of Participants')

# Types of Projects Developed
plt.subplot(1, 3, 2)
sns.barplot(data=projects_df, x='Project Type', y='Count')
plt.title('Types of Projects Developed in Hackathons')
plt.xticks(rotation=45)
plt.xlabel('Project Type')
plt.ylabel('Count')

# Impact on Career Development
plt.subplot(1, 3, 3)
sns.barplot(data=career_impact_df, x='Impact Category', y='Value')
plt.title('Impact of Hackathons on Career Development')
plt.xticks(rotation=45)
plt.xlabel('Impact Category')
plt.ylabel('Value')

plt.tight_layout()
plt.show()

