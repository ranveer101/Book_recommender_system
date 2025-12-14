from flask import Flask, render_template, request
import pickle
import numpy as np

# ================= LOAD DATA =================
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_scores.pkl', 'rb'))
ratings = pickle.load(open('ratings.pkl', 'rb'))

# ================= APP =================
app = Flask(__name__)

# ================= HOME =================
@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_rating'].values),
        rating=list(popular_df['avg_rating'].values)
    )

# ================= RECOMMEND UI =================
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

# ================= RECOMMEND LOGIC =================
@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('book_name')

    if user_input not in pt.index:
        return render_template('recommend.html', error="Book not found")

    index = np.where(pt.index == user_input)[0][0]

    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_books = []

    for i in similar_items:
        book_title = pt.index[i[0]]

        book_df = books[books['Book-Title'] == book_title].drop_duplicates('Book-Title')

        # ISBN
        isbn = book_df['ISBN'].values[0]

        # Ratings
        rating_df = ratings[ratings['ISBN'] == isbn]

        recommended_books.append({
            'title': book_df['Book-Title'].values[0],
            'author': book_df['Book-Author'].values[0],
            'image': book_df['Image-URL-M'].values[0],
            'avg_rating': round(rating_df['Book-Rating'].mean(), 2),
            'num_rating': rating_df.shape[0]
        })

    return render_template('recommend.html', recommended_books=recommended_books)

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)
