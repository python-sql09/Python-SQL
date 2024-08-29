import json
from collections import defaultdict

def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def compute_scores(data):
    restaurant_scores = defaultdict(lambda: {'total_score': 0, 'count': 0, 'min_score': float('inf'), 'max_score': float('-inf')})
    cuisine_borough_scores = defaultdict(lambda: defaultdict(lambda: {'total_score': 0, 'count': 0, 'min_score': float('inf'), 'max_score': float('-inf')}))

    for restaurant in data:
        name = restaurant['name']
        borough = restaurant['borough']
        cuisine = restaurant['cuisine']
        grades = restaurant['grades']

        for grade in grades:
            score = grade['score']
            restaurant_scores[name]['total_score'] += score
            restaurant_scores[name]['count'] += 1
            restaurant_scores[name]['min_score'] = min(restaurant_scores[name]['min_score'], score)
            restaurant_scores[name]['max_score'] = max(restaurant_scores[name]['max_score'], score)

            cuisine_borough_scores[borough][cuisine]['total_score'] += score
            cuisine_borough_scores[borough][cuisine]['count'] += 1
            cuisine_borough_scores[borough][cuisine]['min_score'] = min(cuisine_borough_scores[borough][cuisine]['min_score'], score)
            cuisine_borough_scores[borough][cuisine]['max_score'] = max(cuisine_borough_scores[borough][cuisine]['max_score'], score)

    # Calculate averages for each restaurant
    restaurant_averages = {name: scores['total_score'] / scores['count'] for name, scores in restaurant_scores.items()}

    # Calculate averages for each cuisine in each borough
    cuisine_borough_averages = {}
    for borough, cuisines in cuisine_borough_scores.items():
        cuisine_borough_averages[borough] = {cuisine: scores['total_score'] / scores['count'] for cuisine, scores in cuisines.items()}

    return restaurant_averages, restaurant_scores, cuisine_borough_averages, cuisine_borough_scores

def main():
    filename = 'restaurant.json'
    data = load_data(filename)

    restaurant_averages, restaurant_scores, cuisine_borough_averages, cuisine_borough_scores = compute_scores(data)

    print("Average score for each restaurant:")
    for name, avg in restaurant_averages.items():
        print(f"{name}: {avg:.2f}")

    print("\nMinimum score for each restaurant:")
    for name, scores in restaurant_scores.items():
        print(f"{name}: {scores['min_score']}")

    print("\nMaximum score for each restaurant:")
    for name, scores in restaurant_scores.items():
        print(f"{name}: {scores['max_score']}")

    print("\nAverage score for each type of cuisine in each borough:")
    for borough, cuisines in cuisine_borough_averages.items():
        for cuisine, avg in cuisines.items():
            print(f"{borough} - {cuisine}: {avg:.2f}")

    print("\nMinimum score for each type of cuisine in each borough:")
    for borough, cuisines in cuisine_borough_scores.items():
        for cuisine, scores in cuisines.items():
            print(f"{borough} - {cuisine}: {scores['min_score']}")

    print("\nMaximum score for each type of cuisine in each borough:")
    for borough, cuisines in cuisine_borough_scores.items():
        for cuisine, scores in cuisines.items():
            print(f"{borough} - {cuisine}: {scores['max_score']}")

if __name__ == "__main__":
    main()