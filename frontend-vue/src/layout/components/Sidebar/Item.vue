<script>
export default {
  name: "MenuItem",
  functional: true,
  props: {
    icon: {
      type: String,
      default: ""
    },
    title: {
      type: String,
      default: ""
    }
  },
  render(h, context) {
    const { icon, title } = context.props;
    const vnodes = [];

    if (icon) {
      vnodes.push(<ion-icon class='sidebar-icon' name={icon} />);
    }

    if (title) {
      vnodes.push(
        <span class='title' slot='title'>
          {title}
        </span>
      );
    }
    return vnodes;
  }
};
</script>

<style scoped>
.sidebar-icon {
  width: 30px;
  height: 30px;
  margin: 10px;
}
.title {
  font-size: 16px;
}
</style>
