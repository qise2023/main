# Calculate the quantum correlations for entangled and not entangled photons
import numpy as np
import matplotlib.pyplot as plt


def coincidence_probability(state, alpha, beta):
    """ given a quantum state, calculate the probability of coincidence detection"""
    if state == "HH+VV":
        prob = 0.5*np.cos(alpha-beta)**2
    elif state == "HH-VV":
        prob = 0.5*np.cos(alpha+beta)**2
    elif state == "HV+VH":
        prob = 0.5*np.sin(alpha+beta)**2
    elif state == "HV-VH":
        prob = 0.5*np.sin(alpha-beta)**2
    elif state == "HH":
        prob = (np.cos(alpha)*np.cos(beta))**2
    elif state == "HV":
        prob = (np.cos(alpha)*np.sin(beta))**2
    elif state == "VH":
        prob = (np.sin(alpha)*np.cos(beta))**2
    elif state == "VV":
        prob = (np.sin(alpha)*np.sin(beta))**2
    return prob


if __name__ == "__main__":
    
    angle = np.arange(0,3.14,0.1)
    markers_beta = [22.5, 22.5, 22.5, 22.5, 
                    67.5, 67.5, 67.5, 67.5, 
                    112.5, 112.5, 112.5, 112.5, 
                    157.5, 157.5, 157.5, 157.5]
    markers_prob0 = [coincidence_probability("HH+VV", 0, markers_beta[0]*3.14/180), 
                    coincidence_probability("HV+VH", 0, markers_beta[0]*3.14/180),
                    coincidence_probability("HH", 0, markers_beta[0]*3.14/180),
                    coincidence_probability("HV", 0, markers_beta[0]*3.14/180),
                    coincidence_probability("HH+VV", 0, markers_beta[4]*3.14/180), 
                    coincidence_probability("HV+VH", 0, markers_beta[4]*3.14/180),
                    coincidence_probability("HH", 0, markers_beta[4]*3.14/180),
                    coincidence_probability("HV", 0, markers_beta[4]*3.14/180),
                    coincidence_probability("HH+VV", 0, markers_beta[8]*3.14/180), 
                    coincidence_probability("HV+VH", 0, markers_beta[8]*3.14/180),
                    coincidence_probability("HH", 0, markers_beta[8]*3.14/180),
                    coincidence_probability("HV", 0, markers_beta[8]*3.14/180),
                    coincidence_probability("HH+VV", 0, markers_beta[12]*3.14/180), 
                    coincidence_probability("HV+VH", 0, markers_beta[12]*3.14/180),
                    coincidence_probability("HH", 0, markers_beta[12]*3.14/180),
                    coincidence_probability("HV", 0, markers_beta[12]*3.14/180)]
    
    markers_prob45 = [coincidence_probability("HH+VV", 45*3.14/180, markers_beta[0]*3.14/180), 
                    coincidence_probability("HV+VH", 45*3.14/180, markers_beta[0]*3.14/180),
                    coincidence_probability("HH", 45*3.14/180, markers_beta[0]*3.14/180),
                    coincidence_probability("HV", 45*3.14/180, markers_beta[0]*3.14/180),
                    coincidence_probability("HH+VV", 45*3.14/180, markers_beta[4]*3.14/180), 
                    coincidence_probability("HV+VH", 45*3.14/180, markers_beta[4]*3.14/180),
                    coincidence_probability("HH", 45*3.14/180, markers_beta[4]*3.14/180),
                    coincidence_probability("HV", 45*3.14/180, markers_beta[4]*3.14/180),
                    coincidence_probability("HH+VV", 45*3.14/180, markers_beta[8]*3.14/180), 
                    coincidence_probability("HV+VH", 45*3.14/180, markers_beta[8]*3.14/180),
                    coincidence_probability("HH", 45*3.14/180, markers_beta[8]*3.14/180),
                    coincidence_probability("HV", 45*3.14/180, markers_beta[8]*3.14/180),
                    coincidence_probability("HH+VV", 45*3.14/180, markers_beta[12]*3.14/180), 
                    coincidence_probability("HV+VH", 45*3.14/180, markers_beta[12]*3.14/180),
                    coincidence_probability("HH", 45*3.14/180, markers_beta[12]*3.14/180),
                    coincidence_probability("HV", 45*3.14/180, markers_beta[12]*3.14/180)]
   
    fig1, ax1 = plt.subplots()
    title_str = 'Alpha: {} Deg'.format("0")
    
    axis_scale = 'linear'

    line1=ax1.plot(angle*180/3.14, coincidence_probability("HH+VV", 0, angle), linewidth=2.0, 
                  label='entangled state = {}'.format("HH+VV"), linestyle='dashdot')
    line2=ax1.plot(angle*180/3.14, coincidence_probability("HV+VH", 0, angle), linewidth=2.0, 
                  label='entangled state = {}'.format("HV+VH"), linestyle='dashed')
    line3=ax1.plot(angle*180/3.14, coincidence_probability("HH", 0, angle), linewidth=2.0, 
                  label='pure state = {}'.format("HH"))
    line4=ax1.plot(angle*180/3.14, coincidence_probability("HV", 0, angle), linewidth=2.0, 
                  label='pure state = {}'.format("HV"))
    
    plt.scatter(markers_beta, markers_prob0, color='black', marker='o', facecolors='none', s=80)
    ax1.set_yscale(axis_scale)
    ax1.set_title(title_str)
    ax1.set_xlabel('Beta (Deg)')
    ax1.set_ylabel("Coincidence Probability")
    fig1.legend(loc=(0.5,0.55))
    plt.grid(True)
    plt.ylim(0,1)
    plt.show()

    fig2, ax2 = plt.subplots()
    title_str = 'Alpha: {} Deg'.format("45")
    
    axis_scale = 'linear'

    line1=ax2.plot(angle*180/3.14, coincidence_probability("HH+VV", 45*3.14/180, angle), linewidth=2.0, 
                  label='entangled state = {}'.format("HH+VV"), linestyle='dashdot')
    line2=ax2.plot(angle*180/3.14, coincidence_probability("HV+VH", 45*3.14/180, angle), linewidth=2.0, 
                  label='entangled state = {}'.format("HV+VH"), linestyle='dashed')
    line3=ax2.plot(angle*180/3.14, coincidence_probability("HH", 45*3.14/180, angle), linewidth=2.0, 
                  label='pure state = {}'.format("HH"))
    line4=ax2.plot(angle*180/3.14, coincidence_probability("HV", 45*3.14/180, angle), linewidth=2.0, 
                  label='pure state = {}'.format("HV"))
    
    plt.scatter(markers_beta, markers_prob45, color='black', marker='o', facecolors='none', s=80)
    ax2.set_yscale(axis_scale)
    ax2.set_title(title_str)
    ax2.set_xlabel('Beta (Deg)')
    ax2.set_ylabel("Coincidence Probability")
    fig2.legend(loc=(0.5,0.55))
    plt.grid(True)
    plt.ylim(0,1)
    plt.show()
