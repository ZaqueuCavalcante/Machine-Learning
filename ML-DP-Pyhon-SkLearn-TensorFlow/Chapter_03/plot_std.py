# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot_std(X_train, X_test, X_train_std, X_test_std):
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(17, 10))

    ax[0,0].scatter(X_train[:, 0], X_train[:, 1])
    ax[0,0].grid()
    ax[0,0].set_xlabel('Petal Length [cm]')
    ax[0,0].set_ylabel('Petal Width [cm]')
    ax[0,0].set_title('Train data before Standard')
    
    ax[0,1].scatter(X_test[:, 0], X_test[:, 1])
    ax[0,1].grid()
    ax[0,1].set_xlabel('Petal Length [cm]')
    ax[0,1].set_ylabel('Petal Width [cm]')
    ax[0,1].set_title('Test data before Standard')
    
    ax[1,0].scatter(X_train_std[:, 0], X_train_std[:, 1])
    ax[1,0].grid()
    ax[1,0].set_xlabel('Petal Length [cm]')
    ax[1,0].set_ylabel('Petal Width [cm]')
    ax[1,0].set_title('Train data after Standard')
    
    ax[1,1].scatter(X_test_std[:, 0], X_test_std[:, 1])
    ax[1,1].grid()
    ax[1,1].set_xlabel('Petal Length [cm]')
    ax[1,1].set_ylabel('Petal Width [cm]')
    ax[1,1].set_title('Test data after Standard')
    
    plt.show()
