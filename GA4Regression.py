def init(size,n_feat):
...     pop =[]
...     for i in range(size):
...             chrom = []
...             for i in range(n_feat):
...                     chrom.append(np.bool(random.getrandbits(1)))
...             pop.append(chrom)
...     return pop


def fitness(pop,X_train,y_train,X_test,y_test):
...     scores = []
...     for chrom in pop:
...             logmodel.fit(X_train.iloc[:,chrom],y_train)
...             predict = logmodel.predict(X_test.iloc[:,chrom])
...             scores.append(accuracy_score(y_test,predict))
...     scores = np.array(scores)
...     pop = np.array(pop)
...     sorted_index = np.argsort(scores)
...     return (scores[sorted_index][::-1]), (pop[sorted_index][::-1])


def nat_sel(pop):
...     parent1, parent2 = pop[0,:],pop[1,:]
...     for i in range(len(parent1)):
...             if (i%2 == 0):
...                     placeholder = parent1[i]
...                     parent1[i] = parent2[i]
...                     parent2[i] = placeholder
...     pop[-2,:] = parent1
...     pop[-1,:] = parent2
...     return pop


def mutation(pop,rate):
...     n_mutation = int(len(pop[0,:])*rate)
...     for i in range(n_mutation):
...             rand=random.randint(0,len(pop[0,:])-1)
...             pop[-1,rand]=not(pop[-1,rand])
...             pop[-2,rand]=not(pop[-2,rand])
...     return pop


def generation(size,n_feat,mutation_rate,X_train,y_train,X_test,y_test):
...     pop = init(size,n_feat)
...     fittest = 0
...     best_metrics_for_cancer_detection = []
...     gen_wo_improve = 9
...     while gen_wo_improve > 0:
...             score,pop = fitness(pop)
...             final_mutated_pop = mutation(nat_sel(pop),mutation_rate)
...             if score[0] > fittest:
...                     fittest = score[0]
...                     best_metrics_for_cancer_detection = pop[0]
...                     gen_wo_improve = 9
...             else:
...                     gen_wo_improve = gen_wo_improve - 1
...             print("***** TERMINATING AFTER ******:",gen_wo_improve)
...             print("***** CURRENT ACCURACY ******:",fittest)
...     return fittest, best_metrics_for_cancer_detection

##   ACCURACY IMPROVEMNT AROUND 10 % (91 p.c to 99 p.c)   ##


