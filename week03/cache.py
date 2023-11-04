def solution(cacheSize, cities):
    answer = 0
    cache,clock = [],[]

    for city in cities:
        city = city.upper()
        if cacheSize ==0:
            return len(cities)*5
        if cache and city in cache:
            answer += 1
            del cache[cache.index(city)]
            cache.append(city)
        elif len(cache) < cacheSize:
            cache.append(city)
            answer += 5
        else: 
            del cache[0]
            cache.append(city)
            answer+=5

    return answer