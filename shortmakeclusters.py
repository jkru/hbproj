import clus

def initialize_clusters():
    recipe, ingredients, data = clus.readfile('shortformattedforclusters.txt')
    kclust = clus.kcluster(data,k=50)
    return [recipe, ingredients, data, kclust]


def write_clusters(kclust):
    for i, cluster in enumerate(kclust):
        name = "cluster"+str(i)+".txt"
        f = open("short/"+name, 'w')
        for item in cluster:
            f.write(str(item)+"\n")

def main():
    recipe, ingredients, data, kclust = initialize_clusters()
    print "kclust = "
    print kclust
    write_clusters(kclust)


if __name__=="__main__":
    main()
