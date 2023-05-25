import itertools
from collections import defaultdict

def load_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            community, population, regions, languages, beliefs = line.strip().split(',')
            data.append({
                'community': community,
                'population': int(population),
                'regions': regions.split(';'),
                'languages': languages.split(';'),
                'beliefs': beliefs.split(';')
            })
    return data

def find_associations(data):
    associations = defaultdict(int)

    for community in data:
        for i in range(1, len(community['languages'])+1):
            language_combinations = list(itertools.combinations(community['languages'], i))
            for combination in language_combinations:
                associations[combination] += 1

        for i in range(1, len(community['beliefs'])+1):
            belief_combinations = list(itertools.combinations(community['beliefs'], i))
            for combination in belief_combinations:
                associations[combination] += 1

    return associations

def main():
    file_name = 'comunidades_indigenas.txt'
    data = load_data(file_name)
    associations = find_associations(data)

    print("Asociaciones encontradas:")
    for association, count in associations.items():
        print(f"{association}: {count}")

if __name__ == '__main__':
    main()
