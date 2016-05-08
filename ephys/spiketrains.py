import numpy as np

def get_spiketrain(rec,samps,clu,spikes,window,fs):
    '''
    Returns a numpy array of spike times for a single cluster 
        within a window locked to a sampling time.
    
    Parameters
    ------
    rec : int
        the recording to look in
    samps : int
        the time to lock the spiketrain to in samples
    clu : int
        the cluster identifier to get spikes from
    spikes : pandas dataframe
        the pandas dataframe containing spikes (see core)
    window : tuple or list of floats
        the window around the event in seconds to sample spikes
    fs : float
        sampling rate of the recording
    
    Returns
    ------
    spike_train : numpy array of spike times in seconds
    '''
    bds = [w*fs+samps for w in window]

    window_mask = (
        (spikes['time_samples']>bds[0])
        & (spikes['time_samples']<=bds[1])
        )
    
    perievent_spikes = spikes[window_mask]
    
    mask = (
        (perievent_spikes['recording']==rec)
        & (perievent_spikes['cluster']==clu)
        )
    return (perievent_spikes['time_samples'][mask].values.astype(np.float_) - samps) / fs