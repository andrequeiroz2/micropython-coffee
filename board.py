import network
import ubinascii

topic_pub = ['temperature', 'humidity']


def getMacAddress():
    mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
    return mac


def factory_topic_pub():
    topics_pub = factory_topic_composer(topic_pub)
    return topics_pub


def factory_topic_composer(args):
    topic = []
    topics = []
    for i in range(len(args)):
        topic = args[i]
        topic_composition = (getMacAddress(), '/', topic)
        agglutinate = ''
        topics.append(agglutinate.join(topic_composition))
    return topics
