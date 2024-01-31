def volume_sphere(r):
    # '''input: r = Input in integer format
    #  output:return Vol of sphere upto two decimals'''
    # YOUR CODE GOES HERE
    Vol = (4 * (22 / 7) * (r ** 3)) / 3
    return round(Vol, 2)


# T = int(input())
R = int(input())
print(float(volume_sphere(int(R))))
