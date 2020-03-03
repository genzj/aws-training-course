const siteAddress = new URL("https://dag18u4hr51kz.cloudfront.net/");

module.exports = {
  plugins: [
    {
      resolve: `gatsby-theme-blog`,
      options: {},
    },
    {
      resolve: `gatsby-plugin-s3`,
      options: {
        bucketName: 'zj-gatsby-demo',
        protocol: siteAddress.protocol.slice(0, -1),
        hostname: siteAddress.hostname,
        enableS3StaticWebsiteHosting: false
      },
    },
    {
      resolve: `gatsby-plugin-canonical-urls`,
      options: {
        siteUrl: siteAddress.href.slice(0, -1),
      }
    }
  ],
  // Customize your site metadata:
  siteMetadata: {
    title: `My Blog Title`,
    author: `My Name`,
    description: `My site description...`,
    social: [
      {
        name: `twitter`,
        url: `https://twitter.com/gatsbyjs`,
      },
      {
        name: `github`,
        url: `https://github.com/gatsbyjs`,
      },
    ],
  },
}
