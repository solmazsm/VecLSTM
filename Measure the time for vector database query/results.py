;==========================================
; Title: Compare times and visualize the results
; Author: 
; Date:   ICDM 2024
;==========================================

comparison_data = {'Vectorization Time': vectorization_time, 'Vector DB Query Time': vector_database_query_time}
df_comparison = pd.DataFrame(list(comparison_data.items()), columns=['Operation', 'Time (seconds)'])


plt.bar(df_comparison['Operation'], df_comparison['Time (seconds)'])
plt.xlabel('Operation')
plt.ylabel('Time (seconds)')
plt.title('Vectorization vs. Vector DB Query Time')
plt.show()
